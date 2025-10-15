'''
This program is a serial version of the Traveling Salesman Problem. This is computed by setting a set of incrementing nodes as cities, and randomply placing them on a plane spaced apart, they then will have connections to every other city in this plane, and the shortest distance between them will be the most optimal. This optimal will be computed from each city as the TSP is done. This then will be repeated until a certain node count is reached. This will only be using numpy to create random places on a map and have things be similar to the parallel version.
'''
import numpy


