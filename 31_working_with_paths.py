from pathlib import Path

# Path(r"C:\Program Files\Microsoft")
# Path("./modules/submodule/b.py")
# Path.home()

path = Path("./modules/subModule/b.py")
print(path.exists())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
print(path)
print(path.absolute())
print(path.with_suffix(".txt"))
