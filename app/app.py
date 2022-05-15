import pytesseract
import translators as ts
import cv2
import PIL.Image
from utils import pdf
import tempfile
from pdf2image import convert_from_path, convert_from_bytes

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

my_config = r'--oem 3 --psm 6'

images = convert_from_bytes(open('/app/images/recipe.pdf', 'rb').read())

img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)


print(img_text)
# print(ts.google(img_text, to_language='en'))
