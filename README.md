# Converters UniConvert Library

Welcome to the UniConvert Library documentation! The UniConvert Library is a Python tool designed for file conversion. It provides support for converting images to PNG format and videos to MP4 format. With this library, you can easily integrate file conversion capabilities into your projects.

## Main Features
- **Image Conversion**: Convert images to the PNG, JPEG, WEBP, BMP, JPG, PDF, GIF and TIFF formats.
- **Video Conversion**: Convert videos to the MP4, AVI, MOV, 3GPP, FLV, WMV, MPG, WEBM and MKV formats.

## How to Use

1. Install the library: ``pip install uniconvert``
2. Import the relevant converters in your Python script.
3. Create instances of the converters and use their convert methods to perform conversions.


A seguir, apresentamos exemplos básicos de uso:

### Conversion of Images
```bash
from uniconvert.img_converter import PNGConverter

converter_img = PNGConverter()

img_path = "path/to/image.jpg"

converted_img_path = converter_img.convert(img_path)

print(f"Converted Image: {img_path} -> {converted_img_path}")
```
OR
```bash
from uniconvert import img_converter

converter_img = img_converter.PNGConverter()

img_path = "path/to/image.jpg"

converted_img_path = converter_img.convert(img_path, replace=True)

print(f"Converted Image: {img_path} -> {converted_img_path}")
```
If you want that converted file replace the original then you can use ``replace=True`` in convert method.

### Converting Videos
```bash
from uniconvert.video_converter import MP4Converter

# Cria uma instância do conversor
video_converter = MP4Converter()

# Converte um vídeo para MP4
video_path = "caminho/do/video.avi"
converted_video_path = video_converter.convert(video_path, replace=True)

print(f"Converted Video: {video_path} -> {converted_video_path}")
```

All the other conversion classes follow the same pattern. You just need to specify the extension name, for example, ``MP4Converter()``,``AVIConverter()``, ``GPP3Converter()``, and so on.

### Video Supported Extensions:

- AVI
- MOV
- 3GPP
- FLV
- WMV
- MPG
- WEBM
- MKV

### Image Supported Extensions:
- PNG
- JPEG
- WEBP
- BMP
- JPG
- PDF
- GIF
- TIFF

# Roadmap
We are committed to expanding the functionalities of this library. Planned future enhancements include:

- Support for audio file conversion.
- Creation of specific classes for each file type.

# Contact
Email: dudulj@live.com

GitHub: edududs

# License
MIT License

Copyright (c) 2023 Eduardo Lima de Jesus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
