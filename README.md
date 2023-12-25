# Converters Dud's Library

Welcome to the Converters Dud's Library documentation! The Conversores Dudu Library is a Python tool designed for file conversion. It provides support for converting images to PNG format and videos to MP4 format. With this library, you can easily integrate file conversion capabilities into your projects.

## Main Features
- **Image Conversion**: Convert images to the PNG format effortlessly.
- **Video Conversion**: Convert videos to the MP4 format with ease.

## How to Use

1. Install the library: ``pip install conversores-dudu``
2. Import the relevant converters in your Python script.
3. Create instances of the converters and use their convert methods to perform conversions.


A seguir, apresentamos exemplos básicos de uso:

### Conversion of Images to PNG
```bash
from nome_do_seu_projeto.converters import PNGConverter


# Cria uma instância do conversor
img_converter = PNGConverter()

# Converte uma imagem para PNG
img_path = "caminho/da/imagem.jpg"
converted_img_path = img_converter.convert(img_path)

print(f"Imagem convertida: {img_path} -> {converted_img_path}")
```

### Converting Videos to MP4
```bash
from nome_do_seu_projeto.converters import MP4Converter

# Cria uma instância do conversor
video_converter = MP4Converter()

# Converte um vídeo para MP4
video_path = "caminho/do/video.avi"
converted_video_path = video_converter.convert(video_path)

print(f"Vídeo convertido: {video_path} -> {converted_video_path}")
```
# Roadmap
We are committed to expanding the functionalities of this library. Planned future enhancements include:

- Support for audio file conversion.
- Creation of specific classes for each file type.

# Contact
Email: dudulj@live.com
GitHub: edududs