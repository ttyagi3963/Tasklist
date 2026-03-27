
from pathlib import Path
file_path = Path('files/data.txt')
file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.touch(exist_ok=True)

def to_number(value):
    try:
       return int(value)
    except ValueError:
        return None

def read_file():
    with file_path.open('r') as f:
        file_content = f.readlines()
        return file_content


def get_average():
    file_content =  read_file()
    clean_content = [to_number(n.strip()) for n in file_content if to_number(n) is not None]
    print(clean_content)
    try:
        average = sum(clean_content)/len(clean_content)
        return average
    except ZeroDivisionError:
        return "length of file cant be zero"
    except Exception:
        return "length of file cant be xero"



print(get_average())

