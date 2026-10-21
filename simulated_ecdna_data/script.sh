#!/bin/bash
#SBATCH -n 1
#SBATCH -t 120:0:0
#SBATCH --mem-per-cpu=2G
#SBATCH -J gene_exp_sims
#SBATCH -a 1-225

INPUT_ARGS=$(sed -n "${SGE_TASK_ID}p" list_of_args.txt)
module load miniforge
module load gcc
mamba activate geneExp-rocky9
python exps.py $INPUT_ARGS
