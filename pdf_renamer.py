import re
import os
import slate3k
from PyPDF2 import PdfFileReader, PdfFileWriter

def get_dlv(name):
    with open(name, 'rb') as f:
        doc = slate3k.PDF(f)
        dlv = 'DLV[\d]{5}'
        result = re.search(dlv, doc[0])
        return result.group(0)

def pdf_rename(path):
    with open(f"{path.replace('.pdf','_')}{get_dlv(path)}.pdf", 'wb') as fh:
        pdf_read = PdfFileReader(path)
        pdf_write = PdfFileWriter()
        for page in range(pdf_read.getNumPages()):
            pdf_write.addPage(pdf_read.getPage(page))
        pdf_write.write(fh)


if __name__ == '__main__':
    dirs = os.listdir()
    for file in dirs:
        if re.match('.+.pdf', file):
            pdf_rename(file)
