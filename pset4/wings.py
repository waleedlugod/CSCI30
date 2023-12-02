#!/usr/bin/env python3

class Vertex:
    def __init__(self, label):
        self.label: str = label
        self.neighbors: list[Vertex] = []
        self.visited = False
        
    def addNeighbor(self, vertex):
        self.neighbors.append(vertex)

def TopoDFS(graph: dict[str, Vertex], wing: Vertex, order: list[str]):
    wing.visited = True
    for neighbor in wing.neighbors:
        if not neighbor.visited: TopoDFS(graph, neighbor, order)
    order.append(wing.label)
    return

def check_ordering(obs, ordering):
    # assign index to each vertex in `ordering`
    index = {ordering[i]: i for i in range(len(ordering))}
    
    valid = True
    for (u, v) in obs:
        valid = valid and index[u] < index[v]
    return ordering if valid else None

def arrange_wings(wings: list[str], obs: list[tuple[str, str]]):
    obsGraph = {wings[i]: Vertex(wings[i]) for i in range(len(wings))}
    for ob in obs:
        obsGraph[ob[0]].addNeighbor(obsGraph[ob[1]])
    order = []
    for wing in obsGraph.values():
        if not wing.visited: TopoDFS(obsGraph, wing, order)
    return check_ordering(obs, order[::-1])


### DON'T touch anything below this line
#   this already takes care of the input and output
if __name__ == '__main__':
    n = int(input())
    wings = list(input().split())
    assert n == len(wings), 'length of wings list do not match'

    m = int(input())
    obs = []
    for _ in range(m):
        di, dj = input().split()
        obs.append((di, dj))
    assert m == len(obs), 'length of observations list do not match'

    ordered_wings = arrange_wings(wings, obs)
    if ordered_wings is None:
        print('IMPOSSIBLE')
    else:
        print('\n'.join(ordered_wings))
