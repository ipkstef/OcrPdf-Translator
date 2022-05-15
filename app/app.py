import pytesseract
import translators as ts
import cv2
import PIL.Image


my_config = r'--oem 3 --psm 6'

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

print(dir_path)

# img_text = pytesseract.image_to_string(PIL.Image.open('/app/images/engtest.png'), config=my_config)

# print(ts.google(img_text, to_language='es'))