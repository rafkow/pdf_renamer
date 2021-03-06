import re
import os
import slate3k
import shutil


def get_ext(name):
    with open(name, 'rb') as f:
        doc = slate3k.PDF(f)
        dlv = r'(DLV|LONTL)\d{5}'
        result = re.search(dlv, doc[0])
        if result:
            return result.group(0)


def file_name_trim(name):
    pattern = r'(DTI-E\d|ISF)-(XH-)?\d{8}'
    if result := re.search(pattern, name):
        return result.group(0)


if __name__ == '__main__':
    dirs = os.listdir()
    for file in dirs:
        if re.match('.+.pdf', file):
            if prefix := file_name_trim(file):
                if extension := get_ext(file):
                    new_name = f"{prefix}-{extension}.pdf"
                    if not os.path.exists(new_name):
                        shutil.copy(file, new_name)

