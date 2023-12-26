from __future__ import annotations

from pathlib import Path

from templates.base_converters import BaseIMGConverter, BaseVideoConverter


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


class MP4Converter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the MP4 format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "MP4".

        Returns:
            The converted file.
        """
        target_format = "MP4"
        return super().convert(file_path, target_format, replace)


class AVIConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the AVI format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "AVI".

        Returns:
            The converted file.
        """
        target_format = "AVI"
        return super().convert(file_path, target_format, replace)


class WEBMConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the WEBM format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "WEBM".

        Returns:
            The converted file.
        """
        target_format = "WEBM"
        return super().convert(file_path, target_format, replace)


class MPGConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the MPG format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "MPG".

        Returns:
            The converted file.
        """
        target_format = "MPG"
        return super().convert(file_path, target_format, replace)


class MOVConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the MOV format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "MOV".

        Returns:
            The converted file.
        """
        target_format = "MOV"
        return super().convert(file_path, target_format, replace)


class WMVConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the WMV format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "WMV".

        Returns:
            The converted file.
        """
        target_format = "WMV"
        return super().convert(file_path, target_format, replace)


class FLVConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the FLV format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "FLV".

        Returns:
            The converted file.
        """
        target_format = "FLV"
        return super().convert(file_path, target_format, replace)


class GPPConverter(BaseVideoConverter):
    def convert(self, file_path, target_format="", replace: bool = False) -> Path:
        """
        Convert the given file to the GPP format.

        Args:
            file_path (str): The path to the file to be converted.
            target_format (str, optional): The format to convert the file to. Always "GPP".

        Returns:
            The converted file.
        """
        target_format = "3GPP"
        return super().convert(file_path, target_format, replace)


if __name__ == "__main__":
    converter = MP4Converter()
    converter.convert(
        r"C:\Users\Eduardo Lima\Documents\League of Legends\Highlights\13-22_BR1-2834931132_01.webm",
        replace=True,
    )
