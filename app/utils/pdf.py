from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
import PIL.Image



from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import tempfile

tempdir = tempfile.gettempdir()

class InputPdf():
    def __init__(self):
        self.pdf = None
        self.pages = []

    def load(self, pdf_file):
        self.pdf = pdf_file
        self.pages = convert_from_path(pdf_file)
    
    def get_images(self):
        images = []
        for page in self.pages:
            images.append(page)
        return images
        
    def get_text(self, config):
        text = []
        pages = self.pages
        for page in pages:
            text.append(pytesseract.image_to_string(page, config=config, lang='eng'))
            # text.append(pytesseract.image_to_string(PIL.Image(open(self.get_images)), config=config)
            # text.append(pytesseract.image_to_string(page, config=config))
        return text

    def get_page_count(self):
        return len(self.pages)

    def _save_images(self, path):
        self.path = path
        page_number = 1
        try:
            for page in self.pages:
                page.save(path + '/' + f'{str(page)}' + f'{str(page_number)}.png')
                page_number += 1
        except Exception as e:
            print(e)
            return False
        



