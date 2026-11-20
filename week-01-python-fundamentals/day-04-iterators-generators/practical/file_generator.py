## File Generator

## import path
from pathlib import Path

## method to read file
def file_generator(file_path):
    path = Path(file_path)
    if not path.is_absolute() and not path.exists():
        path = Path(__file__).parent / path

    with path.open("r", encoding="utf-8") as file_handler:
        for line in file_handler:
            ## taking only ERROR
            if "ERROR" in line:
                # using yield
                yield line
                
## test
for line in file_generator("sample.log"):
        ## using end = '' may stop to produce blank lines between records.
        print(line, end="") 
