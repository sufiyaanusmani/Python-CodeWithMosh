from pathlib import Path
from zipfile import ZipFile

# # creating zip file
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("./modules").rglob("*.*"):
#         zip.write(path)
    

# reading and extracting zip file
# with ZipFile("files.zip") as zip:
#     print(zip.namelist())
#     info = zip.getinfo("modules/a.py")
#     print(info.file_size)
#     print(info.compress_size)
    # zip.extractall("extract")

# with ZipFile('p.zip') as myzip:
#     myzip.extractall("ab")