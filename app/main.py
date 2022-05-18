import tempfile
from textwrap import wrap

import pytesseract as pt
from pdf2image import convert_from_path

from utils import pdf

user_input = input("Enter PDF file location: ")
my_config = r"--oem 3 --psm 6"
newfile = tempfile.NamedTemporaryFile(delete=False, suffix="txt")
Pdf = pdf.InputPdf()
Pdf.load()
# Pdf.load(user_input)


def main():
    with tempfile.TemporaryDirectory() as path:

        img_tmp = convert_from_path(Pdf.pdf, output_folder=path, fmt="png")

        for img in img_tmp:
            text = pt.image_to_string(img, config=my_config)
            wrapped = wrap(text, width=15000)
            for line in wrapped:
                # print(line)
                Pdf.pages.append(line)

    print(f"Page Count: {Pdf.page_count()}")
    print(f"pdf text: {Pdf.pages}")
    Pdf.translate("en")
    newfile.close()


if __name__ == "__main__":
    main()
