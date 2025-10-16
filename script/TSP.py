'''
This program is a serial version of the Traveling Salesman Problem. This is computed by setting a set of incrementing nodes as cities, and randomply placing them on a plane spaced apart, they then will have connections to every other city in this plane, and the shortest distance between them will be the most optimal. This optimal will be computed from each city as the TSP is done. This then will be repeated until a certain node count is reached. This will only be using numpy to create random places on a map and have things be similar to the parallel version.
'''
import numpy as np

class SerialTSP:
    def __init__(self, nodes):
        self.nodes = nodes
        self.TSPGraph = None

    def CreateGraph(self):
        #Creates a plane with n nodes placed randomly between 10 and 1000 on the graph
        self.TSPGraph = np.random.uniform(10, 1000, (self.nodes, 2)).astype(int)
        return(print(self.TSPGraph))

    def ComputeGraph(self):
        #for length of nodes, calculate distance from current node to all other nodes and back, find best travel then increment
        for i in range(self.nodes):
            diffs = self.TSPGraph - self.TSPGraph[i]
            print(diffs)

        #Build logic to find optimal path using diff, start at 0,0 then go to all other nodes and back for all diffs.
        for j in range(self.nodes):
            #compute distance from one node to the others and back, have to use trig btw
        
        return

def main():
    tsp = SerialTSP(5)
    tsp.CreateGraph()
    tsp.ComputeGraph()

if __name__ == "__main__":
    main()
