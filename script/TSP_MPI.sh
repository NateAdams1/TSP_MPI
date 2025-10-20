#!/bin/bash
#SBATCH --job-name=TSP-MPI
#SBATCH --output=tsp_mpi_%j.out
#SBATCH --error=tsp_mpi_%j.err
#SBATCH --time=1-12:00:00
#SBATCH --ntasks=20          # number of MPI ranks
#SBATCH --nodes=3
#SBATCH --cpus-per-task=1
#SBATCH --mem=16G
#SBATCH --partition=cpu(all)

# Activate conda environment
module load miniconda3
source $(conda info --base)/etc/profile.d/conda.sh
conda activate /mnt/beegfs/hellgate/home/na193353/.conda/envs/tsp_env

# Pass the max_n as a command-line argument (same as ntasks here)
mpiexec -n $SLURM_NTASKS python TSP_MPI.py $SLURM_NTASKS
