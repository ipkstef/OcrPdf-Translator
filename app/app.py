import pytesseract
import translaters as ts 
# import cv2
# import PIL.Image


my_config = r'--oem 3 --psm 6'

img_text = pytesseract.image_to_string(PIL.Image.open('./images/ECL8R.PNG'), config=my_config)

print(ts.google(img_text, to_language='es'))