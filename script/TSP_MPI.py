"""
Parallel MPI version of the Traveling Salesman Problem (TSP).

- Each MPI rank computes one or more TSP problems independently.
- Rank 0 collects all results and writes to a single HDF5 file.
- Maximum n is passed as a command-line argument.
"""

import numpy as np
import time
import h5py
from mpi4py import MPI
import sys

class SerialTSP:
    def __init__(self, nodes):
        self.nodes = nodes
        self.TSPGraph = None
        self.best_distance = float('inf')
        self.best_path = None

    def CreateGraph(self):
        self.TSPGraph = np.random.uniform(10000, 100000, (self.nodes, 2))
        return self.TSPGraph

    def distance(self, i, j):
        return np.linalg.norm(self.TSPGraph[i] - self.TSPGraph[j])

    def RecursiveTSP(self, current, visited, dist):
        if len(visited) == self.nodes:
            total = dist + self.distance(current, 0)
            if total < self.best_distance:
                self.best_distance = total
                self.best_path = visited + [0]
            return
        for next_city in range(self.nodes):
            if next_city not in visited:
                self.RecursiveTSP(
                    next_city,
                    visited + [next_city],
                    dist + self.distance(current, next_city)
                )

    def ComputeGraph(self):
        start_time = time.time()
        self.RecursiveTSP(0, [0], 0)
        elapsed = time.time() - start_time
        return self.best_path, self.best_distance, elapsed


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # --- Read max_n from command-line ---
    if len(sys.argv) > 1:
        max_n = int(sys.argv[1])
    else:
        max_n = 20  # default

    all_n = range(1, max_n + 1)

    # --- Split work across ranks ---
    n_values = list(all_n[rank::size])

    results = []
    for n in n_values:
        print(f"Rank {rank} computing TSP for {n} cities...")
        tsp = SerialTSP(n)
        tsp.CreateGraph()
        path, distance, elapsed = tsp.ComputeGraph()
        results.append((n, path, distance, elapsed))
        print(f"Rank {rank} finished n={n}: distance={distance:.2f}, time={elapsed:.4f}s")

    # --- Gather results at rank 0 ---
    if rank == 0:
        all_results = results
        for r in range(1, size):
            recv = comm.recv(source=r)
            all_results.extend(recv)

        # --- Save all results to a single HDF5 file ---
        with h5py.File("tsp_mpi_results.h5", "w") as f:
            for n_val, path_val, dist_val, time_val in all_results:
                grp = f.create_group(f"n_{n_val}")
                grp.create_dataset("path", data=path_val)
                grp.create_dataset("distance", data=[dist_val])
                grp.create_dataset("time_seconds", data=[time_val])
                print(f"Saved results for {n_val} cities")
    else:
        comm.send(results, dest=0)


if __name__ == "__main__":
    main()
