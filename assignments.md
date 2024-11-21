#### Assignment 1

Create a python script that converts Hartree units to the units given in the [table](http://wild.life.nctu.edu.tw/class/common/energy-unit-conv-table-detail.html)

#### Assignment 2

Create a script that asks for an integer number and then prints information about that number:
  - Is the integer odd or not.
  - Is the integer devisable by 3.
  - Is the integer devisable by 4.
  - Is the integer devisable by 5.

#### Assignment 3

Improve the [car game](https://github.com/fraxy-v/ccpython_course/blob/master/notes.md#cargame) to give more adequate responses to commands. For example, if the car has been already started, the script should reply to the user that the car is already running.

Hint: Use an additional variable to store the current state of the car.

#### Assignment 4

Create a script that computes the mean value of a list of integer numbers. Don't use the built-in `sum` function.

#### Assignment 5

Define a string variable that contains a meaningful text (having multiple words and sentences).
Then print the text in a reverse order, i.e. the order of the words is reversed.

Hint: See `str` methods `split` and `join`.

#### Assignment 6

Create a script that iterates through a list of strings and removes all entries that are anagrams of previous entries. Example:

```["abc", "def", "ghi", "cba", "bac", "fed"] -> ["abc", "def"]```

Hint: Use `sort` to detect duplicates.

#### Assignment 7

Go through and refactor all homework and classwork script files so far such that the code is extracted into meaningful functions where applicable.

#### Assignment 8

Take any Gaussian output [file](https://github.com/fraxy-v/ccpython_course/blob/master/data/Conformes_1_MM_water.log). Write a python script that reads the file and  extracts (with regex) the dipole moment of the molecule.

Hint: Detect the **last** line ` Dipole moment (field-independent basis, Debye):`. Then from the next line get the values of the three components.

#### Assignment 9

Similar to the previous, extract the quadrupole moment form a Gaussian output file. If not done already, try to read the file line by line rather than loading the entire content at once.

#### Assignment 10

Generate Gaussian input files from the given [file](https://github.com/fraxy-v/ccpython_course/blob/master/data/input.txt) for each basis set from the list `basis_sets = {"STO-3G", "3-21G", "6-21G", "4-31G", "6-31G", "6-31G", "6-311G"}`. The generated files should have a file extension `txt`. Using the module `pathlib`, list all files with `txt` suffix (see the `glob` method) and change the suffix to `gjf` (see methods `with_suffix` and `rename`)

#### Assignment 11

Complete the [script](https://github.com/fraxy-v/ccpython_course/blob/master/data/clock_angle.py) and find the angle between the clock arms at a given hour. Check the solution by adding and running the [test](https://github.com/fraxy-v/ccpython_course/blob/master/data/test_clock_angle.py).

#### Assignment 12

For the next task, use Python with the queue system on `node1` (62.44.108.40) while acquainting yourself with the modules `os` and `sys`.

As an alternative to the bash [script](https://github.com/fraxy-v/ccpython_course/blob/master/data/pbs_g16.sh) that is used for running Guassian jobs, complete the python [script](https://github.com/fraxy-v/ccpython_course/blob/master/data/pbs_fibonacci.py) to compute and print the first N [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_sequence) with the help of a `for` loop.

Explanation: The `os` module provides functionality for accessing environment variables through a dictionary called `environ` and for changing the working directory. The `sys` module allows access to command line arguments, e.g.:
```
python script.py arg1 arg2 arg3
```
In the above case the list `sys.argv` will have 4 entries. The first entry is always the name of the script that is being run followed by command line arguments.

Here the `if __name__ == '__main__':` construction is used to isolate code that is supposed to be executed only directly. That is, if the file is imported as a module this code will be skipped.

Hint: The Python3 version on the nodes is a bit old so you may have to change some parts of the code. For example, if you encounter a problem with the formatted string, use the `format` method of `str` as an alternative.

When you log into `node1` and submit the script on the queue like this:
```
qsub -F "10" script.py
```
(`-F` forwards arguments to the script) you should get an output like this:
```
0
1
1
2
3
5
8
13
21
```

#### Assignment 13

Write a script that from a set of keywords for hybrid functionals: {B3LYP, B3P86, O3LYP} and a simple Gaussian input :
```
# HYB_FUNC/6-31G(d)

water energy

0   1
O  -0.464   0.177   0.0
H  -0.464   1.137   0.0
H   0.441  -0.143   0.0
```
generates input files and bash scripts
```
#!/bin/bash
#PBS -N INPUT_NAME
#PBS -lnodes=1:ppn=8:RAM32GB,walltime=1440:00:00
#PBS_O_WORKDIR=`pwd`
 export PBS_O_WORKDIR
 cd $PBS_O_WORKDIR

echo ================== hostfile ========================
cat  $PBS_NODEFILE
echo ============== end hostfile ========================

g16 INPUT_NAME.gjf

rm /storage/users/${USER}/G*
```
The python script must submit those bash scripts to the queue. That can be done with the help of the `os` module:
```
os.popen("qsub my_bash_script.sh")
```

Note: Not all nodes have python installed. When using the parameters `#PBS -lnodes=1:ppn=8:RAM32GB` we essentially request a node that can run a python script.
