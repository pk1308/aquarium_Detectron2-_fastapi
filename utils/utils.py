import base64

from PIL import Image
import io


def decodeImage(imgstring, fileName):
    input_image = Image.open(io.BytesIO(imgstring)).convert("RGB") 
    input_image.save(fileName)

