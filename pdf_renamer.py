import re
import os
import slate3k
import shutil

def get_dlv(name):
    with open(name, 'rb') as f:
        doc = slate3k.PDF(f)
        dlv = 'DLV[\d]{5}'
        result = re.search(dlv, doc[0])
        return result.group(0)


if __name__ == '__main__':
    dirs = os.listdir()
    for file in dirs:
        if re.match('.+.pdf', file):
            shutil.copy(file, f"{file.replace('.pdf','_')}{get_dlv(file)}.pdf")

