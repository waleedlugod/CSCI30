#!/usr/bin/env python3

from heapdict import heapdict

class Vertex:
    def __init__(self, label):
        self.label: int = label
        self.neighbors: list[tuple[Vertex, int]] = []
        self.predecessor = None
        self.key = 0

    #testing stuff
    def __stf__(self):
        return str(self.label)
    def __repr__(self):
        return f"{str(self.label)}"
        
    def addNeighbor(self, vertex, weight):
        self.neighbors.append((vertex, weight))

def widest_barge(n: int, waterways: list[tuple[int, int, int]]) -> list[int]:
    mst = set()
    maxBarges = [0] * n

    # Initialize the graph
    esteros = [Vertex(i) for i in range(n)]
    for way in waterways:
        esteros[way[0]].addNeighbor(esteros[way[1]], way[2])
        esteros[way[1]].addNeighbor(esteros[way[0]], way[2])

    # Initialize max-priority queue
    maxQueue = heapdict()
    for location in esteros:
        maxQueue[location] = 0
    maxQueue[esteros[0]] = -2**63 + 1
    esteros[0].key = 2**63 - 1

    minBarge = 2**63 - 1
    while len(maxQueue) > 0:
        (location, width) = maxQueue.popitem()
        if location.key < minBarge: minBarge = location.key
        maxBarges[location.label] = minBarge
        if location is not esteros[0]: mst = mst.union({(location.predecessor, location)})
        for neighbor in location.neighbors:
            if neighbor[0] in maxQueue and neighbor[1] > neighbor[0].key:
                neighbor[0].predecessor = location
                neighbor[0].key = neighbor[1]
                maxQueue[neighbor[0]] = -neighbor[1]

    return maxBarges[1:]

### DON'T touch anything below this line
#   this already takes care of the input and output
if __name__ == '__main__':
    n, m = map(int, input().split())
    waterways = []
    for _ in range(m):
        u, v, c = map(int, input().split())
        waterways.append((u, v, c))
    result = widest_barge(n, waterways)
    print('\n'.join(map(str, result)))
    
