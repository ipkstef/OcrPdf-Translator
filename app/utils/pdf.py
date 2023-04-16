import translators as ts

# some comments
class InputPdf:
    def __init__(self):
        self.pdf = None
        self.pages = []

    def load(self, pdf_file="/app/images/sample.pdf"):
        self.pdf = pdf_file

    def translate(self, to_language):
        for page in self.pages:
            print(ts.translate_text(page, to_language=to_language, translator='google'))

    def page_count(self):
        return len(self.pages)
