from __future__ import annotations

from pathlib import Path

from templates.base_converters import BaseIMGConverter, BaseVideoConverter


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


class MP4Converter(BaseVideoConverter):
    def convert(self, file_path, target_format="") -> Path:
        """
        Convert the given file to the MP4 format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Defaults to "MP4".

        Returns:
            The converted file.
        """
        target_format = "MP4"
        return super().convert(file_path, target_format)
