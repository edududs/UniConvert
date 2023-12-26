from __future__ import annotations

from pathlib import Path

from uniconvert.base_converters import BaseIMGConverter


class PNGConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "PNG"
        return super().convert(file_path, target_format, replace)


class JPEGConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "JPEG"
        return super().convert(file_path, target_format, replace)


class WEBPConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "WEBP"
        return super().convert(file_path, target_format, replace)


class BMPConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "BMP"
        return super().convert(file_path, target_format, replace)


class JPGConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "JPG"
        return super().convert(file_path, target_format, replace)


class PDFConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "PDF"
        return super().convert(file_path, target_format, replace)


class GIFConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "GIF"
        return super().convert(file_path, target_format, replace)
    

class TIFFConverter(BaseIMGConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the PNG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "PNG".

        Returns:
            The converted file.
        """
        target_format = "TIFF"
        return super().convert(file_path, target_format, replace)