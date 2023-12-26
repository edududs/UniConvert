import os
from pathlib import Path
from typing import List


def get_existent_file_path(file_path: str | Path) -> Path:
    file_path = Path(file_path).resolve()
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} does not exist")
    if not file_path.is_file():
        raise ValueError(f"{file_path} is not a file")
    return file_path


def is_img(file):
    extensoes_suportadas = [".jpg", ".jpeg", ".bmp", ".webp", ".png"]

    # Verifica se o path é um arquivo
    if os.path.isfile(file):
        # Obtém a extensão do arquivo
        _, extensao = os.path.splitext(file)

        # Verifica se a extensão está na lista de extensões suportadas
        if extensao.lower() in extensoes_suportadas:
            return True

    return False



def split_file_path(path: str | Path) -> List[str]:
    """
    Splits a file path into its directory path, file name, and extension.

    Args:
        path (str | Path): The path of the file.

    Returns:
        List[str]: A list containing the directory path, file name, and extension.
    """
    file_path = get_existent_file_path(path)
    directory, file_name = file_path.parent, file_path.stem
    extension = file_path.suffix
    return [str(directory), str(file_name), extension]


def build_file_path(directory: str | Path, file_name: str, extension: str) -> Path:
    """
    Builds a file path from its directory path, file name, and extension.

    Args:
        directory (str | Path): The directory path.
        file_name (str): The name of the file.
        extension (str): The file extension.

    Returns:
        str: The complete file path.
    """
    # Convert directory to Path if it's given as a string
    directory_path = Path(directory) if isinstance(directory, str) else directory

    # Join the directory, file name, and extension to form the complete file path
    file_path = directory_path / f"{file_name}{extension}"

    return file_path






