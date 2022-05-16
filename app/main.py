# import translators as ts
from importlib.resources import path
import cv2
import pytesseract
from utils import pdf
import tempfile
import os
from pdf2image import convert_from_path
import PIL.Image


my_config = r'--oem 3 --psm 6'
newfile = tempfile.NamedTemporaryFile(delete=False, suffix='txt')
Pdf = pdf.InputPdf()
Pdf.load('/app/images/citizen.pdf')
def main():
    path = '/app/images/excerpts/'
    convert_from_path(Pdf.pdf, output_folder=path, fmt='png')

    image_paths = []
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            image_paths.append(path + filename)
   

    for image_path in image_paths:
        with open(path + 'images.txt', 'a') as file:
            file.write(image_path + '\n')
    print(image_paths)
    text = pytesseract.image_to_string(path + 'images.txt', config=my_config, lang='ita')
    print(text)

    
        






    # print(ts.google(img_text, to_language='en'))
    # img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)

if __name__ == '__main__':
    main()