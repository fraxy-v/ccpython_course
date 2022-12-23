# Replace in file content

from pathlib import Path

p = Path("test.gjf")

with p.open("r") as f:
    contents = f.read()

contents = contents.replace("B3LYP", "B3P86")

with open("testB3P86.gjf", "w") as f:
    contents = f.write(contents)
