from __future__ import annotations

import os

from abc import ABC, abstractmethod
from pathlib import Path

import moviepy.editor as moviepy
from PIL import Image
from utils import build_file_path, is_img, split_file_path


class Conversor(ABC):
    def __init__(self, target_format: str = "") -> None:
        """
        Initializes the class with an optional target format.

        Parameters:
            target_format (str): The format to which the data will be converted. Defaults to an empty string.

        Returns:
            None
        """
        self._target_format = target_format.upper()

    @abstractmethod
    def convert(
        self, file_path: str | Path, target_format: str = "", replace: bool = False
    ) -> Path:
        """Common conversion logic for all converters."""


class ConverterMixin(Conversor):
    def rename_file(self, file_path: str | Path, new_name: str) -> Path:
        """
        Renomeia o arquivo de imagem com um novo nome.

        Esta função renomeia um arquivo de imagem no caminho fornecido, atribuindo
        um novo nome baseado no parâmetro 'new_name'. Se o novo nome já existir,
        o arquivo existente será removido antes da renomeação.

        Parameters:
            file_path (str | Path): O caminho para o arquivo de imagem a ser renomeado.
            new_name (str): O novo nome a ser atribuído ao arquivo.

        Returns:
            Path: O novo caminho para o arquivo de imagem renomeado.
        """

        # Obtém o diretório e o nome do arquivo sem extensão
        *_, ext = split_file_path(file_path)
        dir_file_path = Path(file_path).parent
        new_name = f"{new_name}{ext}"
        new_file_path = Path(dir_file_path, new_name)
        os.rename(file_path, new_file_path)

        return new_file_path

    def generate_temp_out_path(self, file_path):
        """
        Generate a new output path based on the file's path.

        Parameters:
            file_path (str): The path to the input image file.

        Returns:
            str: The new output path.
        """
        # Cria o novo caminho com a extensão correta
        file_name = Path(file_path).stem
        output_directory = Path(file_path).parent
        output_name = f"{file_name}_converted.{self._target_format.lower()}"
        output_path = Path(output_directory, output_name)
        return output_path

    def process_path(self, directory: str | Path) -> None:
        """
        Process the given directory or path.

        Args:
            directory (str | Path): The directory or path to be processed.

        Returns:
            None: This function does not return anything.
        """
        # Transforma o diretório em um Path
        directory = Path(directory).resolve()

        # Verifica se o diretório é um arquivo
        if directory.is_file():
            self.convert(directory)
            return

        # Percorre todos os arquivos no diretório
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)

            # Verifica se é um arquivo e se é uma imagem
            if is_img(file_path):
                self.convert(file_path)


class BaseIMGConverter(ConverterMixin):
    def __init__(self, target_format="") -> None:
        """
        Initializes the class with an optional target format.

        Parameters:
            target_format (str): The format to which the data will be converted. Defaults to an empty string.

        Returns:
            None
        """
        super().__init__()
        self._supported_extensions = self.get_supported_extensions()

    def get_supported_extensions(self) -> set:
        """
        Returns a set of supported extensions by Pillow.

        Returns:
            set: A set of supported extensions.
        """
        # Get the registered extensions from Pillow
        extensions = Image.registered_extensions()

        return set(extensions)

    def convert(self, file_path: str | Path, target_format=None, replace=False) -> Path:
        """
        Common conversion logic for all converters.

        Parameters:
            file_path (str): The path to the input file.
            target_format (str): The target format for conversion. If not provided,
                                the format is determined based on the file extension.

        Raises:
            FileNotFoundError: If the input file does not exist.
            ValueError: If the target format is not supported.
        """

        directory, file_name, ext = split_file_path(file_path)
        # Se o formato alvo não for fornecido, tenta determinar automaticamente com base na extensão
        self._target_format = target_format = (
            target_format.upper() if target_format else ext[1:].upper()
        )

        # Abre a imagem e a salva no formato alvo
        img = Image.open(build_file_path(directory, file_name, ext))

        # Salva como _converted.target_format por padrão
        temp_file = self.generate_temp_out_path(file_path)
        img.save(temp_file, format=target_format)
        img.close()

        if not replace:
            print(f"Imagem convertida: {file_path} -> {temp_file}")
            return temp_file

        ext = f".{target_format.lower()}"
        new_path = build_file_path(directory, file_name, ext)
        os.rename(temp_file, new_path)
        os.remove(file_path)
        print(f"Imagem convertida: {file_path} -> {new_path}")

        return new_path


class BaseVideoConverter(ConverterMixin):
    CODECS = (
        ("MP4", "libx264"),
        ("WEBM", "libvpx"),
        ("MOV", "mov"),
        ("MPEG-1", "mpeg1video"),
        ("MPEG-2", "mpeg2video"),
        ("MPG", "mpeg2video"),
        ("MPEGPS", "mpeg2video"),
        ("MPEG4", "mpeg4"),
        ("AVI", "msmpeg4"),
        ("WMV", "wmv2"),
        ("FLV", "flv"),
        ("3GPP", "h263p"),
    )

    def convert(
        self, file_path: str | Path, target_format: str = "", replace: bool = False
    ) -> Path:
        """
        Convert the given file to the specified format.

        Parameters:
            file_path (str): The path to the file to be converted.
            target_format (str): The format to which the file will be converted.

        Returns:
            The converted file.
        """
        directory, file_name, ext = split_file_path(file_path)
        temp_file = self.generate_temp_out_path(file_path)

        codec = self.codec_of(target_format)
        video_clip = moviepy.VideoFileClip(file_path)
        video_clip.write_videofile(temp_file, codec=codec)
        video_clip.close()
        if not replace:
            print()
            print(f"Video convertido: {file_path} -> {temp_file}")
            return temp_file
        ext = f".{target_format.lower()}"
        new_path = build_file_path(directory, file_name, ext)
        os.rename(temp_file, new_path)
        os.remove(file_path)

        return new_path

    def codec_of(self, selected_format: str) -> str:
        """
        Convert the selected format to the corresponding codec.

        Parameters:
            selected_format (str): The format to be converted.

        Returns:
            str: The corresponding codec for the selected format.
        """
        for extension in self.CODECS:
            if selected_format == extension[0]:
                return extension[1]

        raise ValueError(f"Formato {selected_format} não suportado.")

