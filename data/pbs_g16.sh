#!/bin/bash
#PBS -N test1
#PBS -lnodes=1:ppn=8:RAM32GB,walltime=1440:00:00
#PBS -d /home/your_working_directory_here


echo ================== hostfile ========================
cat  $PBS_NODEFILE 
echo ============== end hostfile ========================

g16 input_file_name.gjf

rm /storage/users/${USER}/G*
