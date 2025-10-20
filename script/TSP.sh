#!/bin/bash
#SBATCH --job-name=tsp_serial
#SBATCH --output=tsp_serial_%j.out
#SBATCH --error=tsp_serial_%j.err
#SBATCH --time=01:00:00       # 1 hour
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --partition=cpu(all)

module load miniconda3
source $(conda info --base)/etc/profile.d/conda.sh
conda activate tsp_env

python3 TSP.py 1-20
