# Pattern matching, find basis

import re

with open("test.gjf") as p:
    for line in p.readlines():
        x = re.search("((STO|\d)\-\d+)\+?G\*?", line)
        if x != None :
            print(x.group())
