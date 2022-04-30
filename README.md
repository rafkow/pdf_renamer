# PDF Renamer

## Issue
All read file have warning
```commandline
WARNING:root:Unknown operator: 'qQq'
```
Disable log warning
```python
venv/Lib/site-packages/pdfminer/psparser.py

def handle_error(exctype, msg, strict=STRICT):
    if strict:
        raise exctype(msg)
    else:
        pass
        # logging.warning(msg) # coomment this
```



## Vession
- 2.2 
  - change word order
  - protection against creating duplicates
- 2.1 
  - extract LONTL number
- 2 
  - copy file with changed name
- 1 
  - create pdf file with changed name  