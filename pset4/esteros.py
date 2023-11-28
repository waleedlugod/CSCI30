#!/usr/bin/env python3

class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
        self.dist = 0 # initialize estimation
        self.predecessor = None # predecessor in longest path
        
    def addNeighbor(self, vertex, weight):
        self.neighbors.append((vertex, weight))

def widest_barge(n: int, waterways: list[tuple[int, int, int]]) -> list[int]:
    '''
    Given the number of locations `n` and a list of waterways, return a list
    of n-1 integers where the ith integer denotes the width of the largest
    possible barge that can safely travel from location 0 to location i.
    '''
    # dijkstra

    # Initialize graph. Running time: O(n)
    graph = {}
    for i in range(len(waterways)):
        u = graph[waterways[i][0]] if waterways[i][0] in graph else Vertex(waterways[i][0])
        v = graph[waterways[i][1]] if waterways[i][1] in graph else Vertex(waterways[i][1])

        u.addNeighbor(v, waterways[i][2])
        v.addNeighbor(u, waterways[i][2])

        if waterways[i][0] not in graph:
            graph[u.label] = u
        if waterways[i][1] not in graph:
            graph[v.label] = v

    verticesMaxQueue = []

    # print graph for testing
    for key in graph:
        print(f"key: {key}, value: {graph[key].label}, neighbors: {[[neighbor[0].label, neighbor[1]] for neighbor in graph[key].neighbors]}")
    return [0]


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
    
