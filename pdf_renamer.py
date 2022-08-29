from re import search, match
from os import path, listdir
from PyPDF2 import PdfFileReader
from shutil import copy


def get_extension(pdf_content: str):
    """Take number of document read in document content"""
    pattern = r'(DLV|LONTL)\d{5}'
    result = search(pattern, pdf_content)
    if result:
        return result.group(0)


def file_name_prefix(name):
    """Take begin leters from file name"""
    pattern = r'(DTI-E\d|ISF)-(XH-)?\d{8}'
    if result := search(pattern, name):
        return result.group(0)


if __name__ == '__main__':
    files = listdir()
    for file in files:
        if match('.+.pdf', file):   # get files with .pdf extension
            if prefix := file_name_prefix(file):
                try:
                    with open(file, 'rb') as f:
                        doc = PdfFileReader(f)
                        text = doc.getPage(0).extractText()
                        if extension := get_extension(file):
                            new_name = f"{prefix}-{extension}.pdf"
                            if not path.exists(new_name):
                                copy(file, new_name)
                except EnvironmentError:
                    pass
                except:
                    pass

