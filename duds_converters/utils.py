import os
from pathlib import Path


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
