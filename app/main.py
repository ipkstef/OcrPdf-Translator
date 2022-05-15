# import translators as ts
import cv2

from utils import pdf
import tempfile


my_config = r'--oem 3 --psm 0'

Pdf = pdf.InputPdf()

def main():
    
    Pdf.load(pdf_file='/app/images/excerpts.pdf', output_folder=tempfile.gettempdir())
    print(Pdf.get_page_count())
    print(Pdf.get_text(config=my_config))







    # print(ts.google(img_text, to_language='en'))
    # img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)

if __name__ == '__main__':
    main()