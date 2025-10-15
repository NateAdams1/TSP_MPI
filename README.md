# Traveling Salesman Problem

This Program is a Brute Force Approach to the [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem). Although there exists better versions of this program done by [Concorde](https://www.math.uwaterloo.ca/tsp/concorde.html), I used this to learn MPI and also understand TSP. There will be a regular serial version of this code, and a parallel version with MPI. This was done at the University of Montana for CSCI 491 Special Topics - HPC with Jacob Downs and run on The University of Montana Hellgate Cluster. 
The project assignment will also be added to display any specifics for the code.

## Code
There are two scripts, one being a serial python script using Numpy and H5PY to have a baseline for the script, and as part as the assignment requirement. There is also a parallel version of the script in python using Numpy, MPI4PY, and H5PY for output.

## How to run
To run the serial version, you will need to create a python environment and install numpy and h5py then run the code in that environment.

To run the parallel version, you will either want to run it on a HPC cluster, or setup a MPI environment to run the code.
