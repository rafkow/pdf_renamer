from re import search, match
from os import path, listdir
from PyPDF2 import PdfFileReader
from shutil import copy


def get_ext(name):
    with open(name, 'rb') as f:
        doc = PdfFileReader(f)
        dlv = r'(DLV|LONTL)\d{5}'
        result = search(dlv, doc.getPage(0).extractText())
        if result:
            return result.group(0)


def file_name_trim(name):
    pattern = r'(DTI-E\d|ISF)-(XH-)?\d{8}'
    if result := search(pattern, name):
        return result.group(0)


if __name__ == '__main__':
    dirs = listdir()
    for file in dirs:
        if match('.+.pdf', file):
            if prefix := file_name_trim(file):
                if extension := get_ext(file):
                    new_name = f"{prefix}-{extension}.pdf"
                    if not path.exists(new_name):
                        copy(file, new_name)

