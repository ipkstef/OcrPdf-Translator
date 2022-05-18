import pytesseract as pt
from utils import pdf
import tempfile
from pdf2image import convert_from_path
from textwrap import wrap



my_config = r'--oem 3 --psm 6'
newfile = tempfile.NamedTemporaryFile(delete=False, suffix='txt')
Pdf = pdf.InputPdf()
Pdf.load('/app/images/sample.pdf')


def main():
    with tempfile.TemporaryDirectory() as path:

        img_tmp = convert_from_path(Pdf.pdf, output_folder=path, fmt='png')


        for img in img_tmp:
            text = pt.image_to_string(img, config=my_config)
            wrapped = wrap(text, width=15000)
            for line in wrapped:
                # print(line)
                Pdf.pages.append(line)
            
        
    
    
    print(f'Page Count: {Pdf.page_count()}')
    Pdf.translate('am')
    
    newfile.close()


    # print(ts.google(img_text, to_language='en'))
    # img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)

if __name__ == '__main__':
    main()