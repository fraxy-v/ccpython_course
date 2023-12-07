#!/usr/bin/python3
#PBS -N pytest
#PBS -lnodes=1:ppn=1:RAM128GB,walltime=0:01:00
#PBS_O_WORKDIR=`pwd`
import os
import sys

# specifies code that should only be executed when the file is run as the main program, and not when it is imported as a module.
if __name__ == '__main__':
    # change the current directory with os.chdir
    # access to environmental variables with os.environ
    os.chdir(os.environ.get("PBS_O_WORKDIR", "."))

    # sys.argv gives acces to command line arguments
    # sys.argv[0] is always the name of the script that is being executed
    if len(sys.argv) <= 1:
        print(f"{sys.argv[0]} Expects one argument")
        exit(1)

    # get the first argument
    n = int(sys.argv[1])

    # computes and prints first n fibonacci numbers
