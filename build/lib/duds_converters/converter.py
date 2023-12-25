from __future__ import annotations

import os
from abc import ABC, abstractmethod
from pathlib import Path
from utils import get_existent_file_path, is_img

from PIL import Image


class Conversor(ABC):
    @abstractmethod
    def convert(self, file_path: str | Path, target_format: str = "") -> Path:
        """Common conversion logic for all converters."""


class BaseConverter(Conversor):
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
        _file_path = get_existent_file_path(file_path)
        extension = _file_path.suffix
        new_name = f"{new_name}{extension}"
        new_file_path = Path(_file_path.parent, new_name)

        # Remove o novo arquivo se ele já existir
        if new_file_path.exists():
            os.remove(new_file_path)

        # Renomeia o arquivo de imagem
        os.rename(file_path, new_file_path)

        return new_file_path

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


class ConversorManager(ABC):
    @abstractmethod
    def menu(self) -> None:
        """Display the conversion options."""

    @abstractmethod
    def convert(self, caminho_imagem: str, target_format: str) -> None:
        """Convert the image to the specified format."""


class BaseIMGConverter(BaseConverter):
    def __init__(self, target_format="") -> None:
        """
        Initializes the class with an optional target format.

        Parameters:
            target_format (str): The format to which the data will be converted. Defaults to an empty string.

        Returns:
            None
        """
        super().__init__()
        self._target_format = target_format.upper()
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

    def convert(self, file_path: str | Path, target_format=None) -> Path:
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

        _file_path = get_existent_file_path(file_path)
        directory, file_name = _file_path.parent, _file_path.stem
        extensao = _file_path.suffix

        # Se o formato alvo não for fornecido, tenta determinar automaticamente com base na extensão
        target_format = (
            target_format.upper().replace("-", "")
            if target_format
            else extensao[1:].upper()
        )

        # Verifica se o formato alvo é suportado
        # if target_format not in self._supported_extensions:
        #     raise ValueError(f"Unsupported target format: {target_format}")

        # Cria o novo caminho com a extensão correta
        novo_caminho1 = Path(directory, f"{file_name}.{target_format.lower()}")

        # Abre a imagem e a salva no formato alvo
        img = Image.open(_file_path)
        img.save(novo_caminho1, format=target_format)

        img.close()
        # Opcional: Remove o arquivo original
        os.remove(file_path)

        print(f"Imagem convertida: {file_path} -> {novo_caminho1}")
        return novo_caminho1


class PNGConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="") -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Defaults to "PNG".

        Returns:
            The converted file.
        """
        target_format = "PNG"
        return super().convert(file_path, target_format)


if __name__ == "__main__":
    conversor = PNGConverter()
    conversor.convert(
        file_path=r"D:\Eduardo\Downloads\WhatsApp Image 2023-10-05 at 13.43.10.jpeg",
    )
