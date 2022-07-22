import subprocess

# result = subprocess.run(["ls", "-l"])
# print(type(result))

c = subprocess.run(["python", "1_first.py"], capture_output=True, text=True)