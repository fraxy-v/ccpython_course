# Find in file content

from pathlib import Path

p = Path("test.gjf")

f = p.open("r")

for line in f.readlines():
    tokens = line.split()
    if len(tokens) > 0 and tokens[0] == '#':
        print(tokens[1])
