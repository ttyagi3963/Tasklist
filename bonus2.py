filenames = ["1.doc","1.report","1.present"]

new_filenames =[(f"{filename}.txt").replace(".","-",1) for filename in filenames]
print(new_filenames)