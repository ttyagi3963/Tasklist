from pathlib import Path
contents = ['all carrots r red', "the carrots are healthy", 'the carrots need to be eaten every day']
filenames = ["doc.txt","report.txt", "presentation.txt"]



# for index,filename in enumerate(filenames):
#     filepath = Path(f"bonus/{filename}")
#     filepath.parent.mkdir(parents=True, exist_ok=True)
#     with filepath.open('w', encoding="utf-8") as f:
#         f.write(contents[index])


for content, filename in zip(contents, filenames):
    filepath = Path(f"bonus/{filename}")
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with filepath.open('w', encoding="utf-8") as f:
        f.write(content)




