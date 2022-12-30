## Assignment 1: Tidy up repo

Goal: Exercise basic GitHub and git commands.

  - [ ] Remove junk files.
  - [ ] Create folder classwork and move valid Python files to this folder
  - [ ] Delete merged branch (use GitHub)
 
 ## Assignment 2: Find mean value of a list
 
Given a list of numbers, the task is to find the mean value of that list. 

Goal: Exercise Python loops and functions. Please don't use built-in `sum` function.


 - [ ] Create folder `home_assignments`.
 - [ ] Implement function that computes the mean value of a list.
 - [ ] Compare results to `numpy.mean`
 - [ ] Handle the case of an empty list argument.

## Assignment 3: Compute standard deviation of a list

Compute standard deviation, the measure of the spread of the distribution of the values in a list. See https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-population/a/calculating-standard-deviation-step-by-step.

Hint: that's roughly a combination of two tasks that we have already done: mean value and the sum of squares.

Goal: Practice working with modules.
 - [ ] Create a new file for the standard deviation functin.
 - [ ] Import and use the mean value function from #3
 - [ ] Import math module and use the `sqrt` function.
 - [ ] In a new test_std.py file test your standard deviation implementation against `numpy.std`
 - [ ] Make sure that the behavior of your implementation is the same as `numpy.std` when the function argument is an empty list. Modify the implementation of the mean value function if you have to.  (Raise the appropriate python error.)

## Assignment 4: Change extension of file

 Prerequisite: The execution folder of the script contains the files with a given extension.

Change the extension of all files of a given type in the folder.

Goal: Introduction to pathlib module.

 - [ ] Use the `glob` method of `Path` to list all files with a specific extension. `glob` generates a collection of `Path` objects that can be iterated over.
 - [ ] Use the `with_suffix` method of `Path` to produce a new `Path` object with a modified extension. Example: `f.with_suffix('.txt')`
 - [ ] Use `rename` method of `Path` to rename a file. Example: `existingPath.rename(modifiedPath)`

## Assignment 5: Reverse the word order of a text file

Goal: Practice reading/writing to text files.

Go to https://www.loremipzum.com/en/text-generator and generate a random text. Store it in a file. Reverse the word order of this file with a script that you have written. For example, if the input file contains `Lorem ipsum dolor sit`, the result must be `sit dolor ipsum Lorem`

Hint: `read` and `write` methods of the file object can be used to load/store the full content. `' '.join(list)` is the reverse opration of `string.split(' ')`

## Assignment 6: Find the median value of a list of numbers

Goal: Practice working with lists.

Write a method that finds the median value of a list. 
Hint: You don't need to iterate over the values of the list in this one, but you have to prepare the list with a built-in function before finding the value.

 - [ ] Check the input of the function for empty list arguments and raise an appropriate error.
 - [ ] Write your `mean` function.
 - [ ] Test the function against `numpy.mean` in a separate test file.

## Assignment 7: Print the basis set used in a Gaussian input file
Goal: Practice reading of files.

Define a "basis sets" set
```
basis_sets = {"STO-3G", "3-21G", "6-21G", "4-31G", "6-31G", "6-31G", "6-311G"}
```
and detect if the command line of a Gaussian input file (starting with "#") contains a basis set from the set and print which one.


## Assignment 8: Extract all components of the quadrupole moment from a Gaussian output file

Goal: practice data post-processing

Write a script that parses a Gaussian output file and prints the quadrupole moment on the screen.

## Assignment 9: Python script that submits Gaussian tasks on the queue

Goal: practice data pre-processing 

Write a script that from a set of keywords for hybrid functions:  `{B3LYP, B3P86, O3LYP}` and a simple Gaussian input : 

```
# KEYWORD/6-31G(d) 

water energy 

0   1
O  -0.464   0.177   0.0   
H  -0.464   1.137   0.0   
H   0.441  -0.143   0.0
```

generates input files and bash scripts similar to `pbs_g16.sh` and submits them to the queue.
