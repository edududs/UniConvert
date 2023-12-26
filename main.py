from PIL import Image

from uniconvert import img_converter
converter = img_converter.TIFFConverter()
converter.convert(
    r"C:\Users\Eduardo Lima\Pictures\Fotos para zoar\WhatsApp Image 2023-08-22 at 00.54.32.png"
)
