import re
import os
import slate3k
import shutil


def get_ext(name):
    with open(name, 'rb') as f:
        doc = slate3k.PDF(f)
        dlv = 'DLV[\d]{5}'
        result = re.search(dlv, doc[0])
        if result:
            return result.group(0)
        lontl = 'LONTL[\d]{5}'
        result = re.search(lontl, doc[0])
        if result:
            return result.group(0)
        return None


if __name__ == '__main__':
    dirs = os.listdir()
    for file in dirs:
        if re.match('.+.pdf', file):
            extension = get_ext(file)
            if extension:
                shutil.copy(file, f"{file.replace('.pdf','_')}{extension}.pdf")

