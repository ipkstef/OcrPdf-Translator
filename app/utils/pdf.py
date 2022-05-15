class pdf():
    def __init__(self, file_name):
        self.file_name = file_name
        self.pdf = None


    def read(self): 
        self.pdf = pytesseract.image_to_pdf_or_hocr(self.file_name, 'out.pdf', extension='pdf', config=my_config)
        return self.pdf