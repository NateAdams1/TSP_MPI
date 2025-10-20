"""
This program is a serial version of the Traveling Salesman Problem (TSP).
It generates a set of cities placed randomly on a 2D plane and computes the
shortest path visiting all cities exactly once and returning to the start.
The algorithm runs recursively and computes the optimal path for each city
count in a user-specified range. Results are stored in an HDF5 file.
"""

import numpy as np
import time
import h5py

class SerialTSP:
    #Setup global function variables
    def __init__(self, nodes):
        self.nodes = nodes
        self.TSPGraph = None
        self.best_distance = float('inf')
        self.best_path = None

    #creates graph of input nodes in a plane between points 10,000 and 100,000
    def CreateGraph(self):
        self.TSPGraph = np.random.uniform(10000, 100000, (self.nodes, 2))
        return self.TSPGraph

    #Calculates distance between each node
    def distance(self, i, j):
        return np.linalg.norm(self.TSPGraph[i] - self.TSPGraph[j])

    #Recursively calculates each node distance and finds the shortest path
    def RecursiveTSP(self, current, visited, dist):
        if len(visited) == self.nodes:
            total = dist + self.distance(current, 0)  # return to start
            if total < self.best_distance: #if total distance is shorter than best found, update best_diastance
                self.best_distance = total
                self.best_path = visited + [0]
            return

        for next_city in range(self.nodes):
            if next_city not in visited: #skips over visited citites
                self.RecursiveTSP( #recursive call
                    next_city,
                    visited + [next_city],
                    dist + self.distance(current, next_city) #updates total distance
                )

    #Runs the recursive step and times it
    def ComputeGraph(self):
        start_time = time.time()
        self.RecursiveTSP(0, [0], 0)
        elapsed = time.time() - start_time
        return self.best_path, self.best_distance, elapsed


def main():
    #Asks for range of cities
    user_input = input("Enter range of cities (e.g. 3-7): ").strip()
    if "-" in user_input:
        start, end = map(int, user_input.split("-"))
        n_values = range(start, end + 1)
    else:
        n_values = [int(user_input)]

    # --- Create HDF5 file ---
    with h5py.File("tsp_serial_results.h5", "w") as f:
        for n in n_values:
            print(f"\nRunning TSP for {n} cities...")
            tsp = SerialTSP(n)
            tsp.CreateGraph()
            path, distance, elapsed = tsp.ComputeGraph()

            # Save results in HDF5
            grp = f.create_group(f"n_{n}")
            grp.create_dataset("path", data=path)
            grp.create_dataset("distance", data=[distance])
            grp.create_dataset("time_seconds", data=[elapsed])

            print(f"Shortest distance: {distance:.2f}")
            print(f"Execution time: {elapsed:.4f} seconds")

    print("\nResults saved to tsp_serial_results.h5")

if __name__ == "__main__":
    main()
