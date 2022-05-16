# import translators as ts
from importlib.resources import path
import cv2
import pytesseract
from utils import pdf
import tempfile
import os
from pdf2image import convert_from_path
import PIL.Image


my_config = r'--oem 3 --psm 0'
newfile = tempfile.NamedTemporaryFile(suffix='.txt', delete=False)

Pdf = pdf.InputPdf()
Pdf.load('/app/images/excerpts.pdf')
def main():
    path = '/app/images/excerpts/'
    Pdf._save_images(path)
    print(Pdf.get_page_count())
    image_path = []
    for filename in os.listdir(path):
        image_path.append(path + filename)
    with open(path + 'images.txt', 'w') as f:
        for image_path in image_path:
            f.write(image_path + '\n')
    
    pytesseract.image_to_string(path + 'images.txt', config=my_config)
        

    
        






    # print(ts.google(img_text, to_language='en'))
    # img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)

if __name__ == '__main__':
    main()