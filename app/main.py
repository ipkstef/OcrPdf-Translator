import translators as ts
import pytesseract
from utils import pdf
import tempfile
import os
import glob
import time
from pdf2image import convert_from_path
import PIL.Image

from textwrap import wrap



my_config = r'--oem 3 --psm 6'
newfile = tempfile.NamedTemporaryFile(delete=False, suffix='txt')
Pdf = pdf.InputPdf()
Pdf.load('/app/images/excerpts.pdf')
def main():
    path = '/app/images/excerpts/'
    files_png = glob.glob(path + '*.png')
    files_txt = glob.glob(path + '*.txt')
    for f in files_png:
        os.remove(f)
        time.sleep(0.5)
    for f in files_txt:
        os.remove(f)
        time.sleep(0.5)


    convert_from_path(Pdf.pdf, output_folder=path, fmt='png')

    path_list = Pdf.image_paths(path)

    for path in path_list:
        img = PIL.Image.open(path)
        text = pytesseract.image_to_string(img, config=my_config)
        bytes_text = bytes(text, 'utf-8')
        newfile.write(bytes_text)
    
    newfile.close()
    print(newfile.name)

    

   

    
    # text = pytesseract.image_to_string(path + 'images.txt', config=my_config, lang='ita')
    # print(text)
    # wrapped = wrap(text, width=1500)
    # for line in wrapped:
    #     print(ts.google(line, to_language='es'))

    



    
        






    # print(ts.google(img_text, to_language='en'))
    # img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)

if __name__ == '__main__':
    main()