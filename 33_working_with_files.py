from pathlib import Path
from time import ctime
import shutil

path = Path("./modules/a.py")
print(path.stat())
print(ctime(path.stat().st_ctime))

print(path.read_text())
path.write_text("...")

# shutil.copy(source, target)
