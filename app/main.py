import translators as ts
import pytesseract as pt
from utils import pdf
import tempfile
from pdf2image import convert_from_path
from textwrap import wrap



my_config = r'--oem 3 --psm 6'
newfile = tempfile.NamedTemporaryFile(delete=False, suffix='txt')
Pdf = pdf.InputPdf()
Pdf.load('/app/images/excerpts.pdf')


def main():
    with tempfile.TemporaryDirectory() as path:

        img_test = convert_from_path(Pdf.pdf, output_folder=path, fmt='png')

        path_list = Pdf.image_paths(path)

        for img in img_test:
            text = pt.image_to_string(img, config=my_config)
            bytes_text = bytes(text, 'utf-8')
            newfile.write(bytes_text)

        # newfile.close()
        newfile.seek(0)
        print(newfile.read())

       

    # wrapped = wrap(text, width=1500)
    # for line in wrapped:
    #     print(ts.google(line, to_language='es'))


    # print(ts.google(img_text, to_language='en'))
    # img_text = pytesseract.image_to_string(PIL.Image.open(images), config=my_config)

if __name__ == '__main__':
    main()