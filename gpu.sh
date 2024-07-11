#!/bin/bash
#SBATCH -p gpu                      # Specify partition [Compute/Memory/GPU]
#SBATCH -N 1 -c 16   			    # Specify number of nodes and processors per task
#SBATCH --gpus-per-task=1		    # Specify number of GPU per task
#SBATCH --ntasks-per-node=4		    # Specify tasks per node
#SBATCH -t 00:02:00                # Specify maximum time limit (hour: minute: second)
#SBATCH -A lt200291               	# Specify project name
#SBATCH -J wdc-gpu               	# Specify job name

module load Mamba/23.11.0-0         # Load the conda module
conda activate pytorch-2.2.2		# Activate your environment

python3 basic-multi-gpu-pytorch.py  # Run your program or executable code