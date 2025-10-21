# Traveling Salesman Problem

This Program is a Brute Force Approach to the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem). Although there exists better versions of this program done by [Concorde](https://www.math.uwaterloo.ca/tsp/concorde.html), I used this to learn MPI and also understand TSP. There will be a regular serial version of this code, and a parallel version with MPI. This was done at the University of Montana for CSCI 491 Special Topics - HPC with Jacob Downs and run on The University of Montana Hellgate Cluster. 
The project assignment will also be added to display any specifics for the code.

## Code
This Code has 2 scripts, the first one is a serial version of the code, this runs python with numpy and exports to a hdf5 file. The second is a parallel script that runs python using numpy, mpi, and exports to a hdf5 file.
## How to run
### To run the serial version, you will need to create a python environment and install numpy and h5py then run the code in that environment.

```
First you will need to clone this project, then enter to the directory of the script.

git clone https://github.com/NateAdams1/TSP_MPI.git

cd TSP_MPI
cd script

-For Mac / Linux
python3 -m venv venv

-For Windows
python -m venv venv

-This creates a Virtual Environment, from here you will need to activate the environment

-For Mac / Linux
source venv/bin/activate

-For Windows
venv\Scripts\activate

-Now we will need to install required packages

pip install numpy h5py

-Then you can run the script with

python tsp_serial.py

-Deactivate the environment when done

deactivate 
```

### In order to run the parallel version, you will need access to a device or cluster that can run a conda envrionment

```
-First you will need to login to your cluster, or go to a working directory in your MPI worker (Scratch on most clusters)

ssh login@cluster.edu

-Now you will need to navigate to your scratch directory, this differs by cluster but would look like this

cd /path/to/scratch/user

-From here, you can clone by using slurm resources, or sftp, I am going to show using slumr resources with LMOD / modules

module spider git
#This will show available git modules

module load git/version

salloc --nodes=1 --time=1:00:00
#requests a interactive session for one hour on a node

git clone https://github.com/NateAdams1/TSP_MPI.git

-This should clone the github repository, then you will need to navigate to the scripts folder

cd TSP_MPI

cd script

-Here will be found the TSP_MPI.sh file to be run, if you go into the file, the ntasks will be the number of nodes created, it is set to 20 but change that as needed

sbatch TSP_MPI.sh

-This will create a slurm job, you can watch that job update with

watch squeue --me
```

### In order to view the .h5 file you can either run the read_h5.py or use h5dump

```
-If you use 

h5dump

-it will produce a somewhat legible version of the file, or you can navigate to the main directory and run the python file

cd TSP_MPI

-using the previous steps to activate the virtual environment, you just do

read_h5.py
```
