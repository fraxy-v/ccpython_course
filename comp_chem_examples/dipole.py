# Pattern matching, find dipole moment
import re

dipole = {}
with open("Conformes_1_MM_water.log", "r") as f:
    outsideDipole = True
    for line in f.readlines():
        if outsideDipole:
            if line.find("Dipole moment") != -1:
                outsideDipole = False
                continue
        else:
            print(line)
            m = re.findall("\s+(\w+)=\s+(-?\d\.\d+)", line)
            # print(m)
            dipole[m[0][0]] = float(m[0][1])
            dipole[m[1][0]] = float(m[1][1])
            dipole[m[2][0]] = float(m[2][1])
            dipole[m[3][0]] = float(m[3][1])
            outsideDipole = True

print (dipole)
