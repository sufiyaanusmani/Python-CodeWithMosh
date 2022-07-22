from pathlib import Path

path = Path("./modules")

for p in path.iterdir():
    print(p)

pyFiles = [p for p in path.glob("*.py")]
print(pyFiles)

pyFiles = [p for p in path.rglob("*.py")]
print(pyFiles)
