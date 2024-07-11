#!/bin/bash
#SBATCH -p compute      	#specific partition
#SBATCH -N 1 -c 128         #specific number of nodes and cores per task
#SBATCH -t 00:05:00       #job time limit <hr:min:sec>
#SBATCH -A lt200291         #project name
#SBATCH -J wdc-GROMACS      	#job name

##Module Load##
module restore
module load GROMACS/2022.5-GNU-11.2-CUDA-11.7

gmx mdrun -deffnm /project/lt200291-ignite/gromacs/input_file/lignocellulose.tpr