from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
import PIL.Image



from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

import os

class InputPdf():
    def __init__(self):
        self.pdf = None
        self.pages = []

    def load(self, pdf_file):
        self.pdf = pdf_file
        
    
    def image_paths(self, path):
        image_paths = []
        for filename in os.listdir(path):
            if filename.endswith(".png"):
                image_paths.append(path + filename)
        for image_path in image_paths:
            with open(path + 'images.txt', 'a') as file:
                file.write(image_path + '\n')
        return image_paths




        



