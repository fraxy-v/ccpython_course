#Self executing script

#!/usr/bin/python3
#PBS -N pytest
#PBS -lnodes=1:ppn=1:RAM128GB,walltime=0:01:00
#PBS_O_WORKDIR=`pwd`
import os

os.chdir(os.environ.get("PBS_O_WORKDIR"))
var = int(os.environ.get("COUNTER", 10))

if var < 10:
    f = open("test" + str(var) + ".txt", "w")
    f.write(str(var))
    f.close()

    command = "cd user; "
    command += "qsub -v COUNTER=" + str(var + 1) + " hello_world.py"
    command = "ssh node1 '" + command + "'"
    print("Executing: " + command)
    stream = os.popen(command)
    print("qsub output: " +  stream.read())
else:
    print("Done")
