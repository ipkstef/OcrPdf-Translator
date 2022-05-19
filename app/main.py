import tempfile, sys
from textwrap import wrap
from time import perf_counter

import pytesseract as pt
from pdf2image import convert_from_path

from utils import pdf

my_config = r"--oem 3 --psm 6"
Pdf = pdf.InputPdf()


Pdf.load(sys.argv[1])

newfile = tempfile.NamedTemporaryFile(delete=False, suffix="txt")


def main():
    with tempfile.TemporaryDirectory() as path:

        img_tmp = convert_from_path(Pdf.pdf, output_folder=path, fmt="png")

        for img in img_tmp:
            text = pt.image_to_string(img, config=my_config)
            wrapped = wrap(text, width=15000)
            for line in wrapped:
                # print(line)
                Pdf.pages.append(line)
                bytes_text = bytes(line, "utf-8")
                newfile.write(bytes_text)

    print(f"Page Count: {Pdf.page_count()}")
    print(f"pdf text: {Pdf.pages}")
    Pdf.translate("en")
    newfile.close()


if __name__ == "__main__":
    main()
