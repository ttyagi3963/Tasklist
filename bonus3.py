from pathlib import Path
dirPath = Path("Journals/")
dirPath.mkdir(exist_ok=True)

date = input("enter Todays Date : ")
filePath = f"Journals/{date}.txt"
filePath = Path(filePath)

thoughts  = input("what are your thoughts? ")
thoughts  = thoughts + "\n\n"+ "yes" + 2 *"\n" +"Try"
with filePath.open("w") as f:
    f.write(thoughts)