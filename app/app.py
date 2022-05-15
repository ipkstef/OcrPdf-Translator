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

images = convert_from_bytes(open('/app/images/excerpts.pdf', 'rb').read())

for page in images:
    count = 0
    PIL.Image.SAVE(f'/app/images/{page}{count}.png', 'PNG')
    image = cv2.imread(f'/app/images/{page}{count}.png')
    text = pytesseract.image_to_string(image, config=my_config)
    print(text)
    print('\n\n')
    count += 1

# img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)


# print(img_text)
# print(ts.google(img_text, to_language='en'))
