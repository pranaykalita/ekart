from PIL import Image
from io import BytesIO
import os

def resizeProduct_image(image_path, max_size=(270, 274)):
    # Open the image using PIL Image library
    img = Image.open(image_path)

    # Resize the image
    img.thumbnail(max_size)

    # Convert the resized image to bytes
    bytes_io = BytesIO()
    format = os.path.splitext(image_path)[1][1:]
    img.save(bytes_io, format=format)
    image_data = bytes_io.getvalue()

    return image_data, format