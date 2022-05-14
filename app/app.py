import pytesseract
import cv2
import PIL.Image


my_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(PIL.Image.open('./images/ECL8R.PNG'), config=my_config)

print(text)