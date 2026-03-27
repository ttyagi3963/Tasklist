from pathlib import Path

file_path = Path("files/docs.txt")

file_path.parent.mkdir(parents=True, exist_ok=True)

file_path.touch(exist_ok=True)

with file_path.open("r") as f:
    f.read()






