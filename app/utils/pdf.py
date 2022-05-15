from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
import PIL.Image



from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import tempfile



class InputPdf():
    def __init__(self):
        self.pdf = None
        self.pages = []

    def load(self, pdf_file, output_folder=None):
        self.pdf = pdf_file
        images = convert_from_bytes(open(pdf_file, 'rb', output_folder).read())
        for image in images:
            self.pages.append(image)
    
    def get_images(self):
        images = []
        for page in self.pages:
            images.append(page)
        return images
        
    def get_text(self, config):
        text = []
        for page in self.pages:
            text.append(pytesseract.image_to_string(PIL.Image.read(page), config=config))
            # text.append(pytesseract.image_to_string(page, config=config))
        return text

    def get_page_count(self):
        return len(self.pages)

    def save_images(self, path):
        page_number = 1
        for page in self.pages:
            page.save(path + '/' + f'{str(page)}' + f'{str(page_number)}.png')
            page_number += 1


