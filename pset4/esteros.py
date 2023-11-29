#!/usr/bin/env python3

def find(forest: list[set[int]], leaf: int) -> set[int]:
    for tree in forest:
        if leaf in tree:
            return tree
    return {leaf}

def widest_barge(n: int, waterways: list[tuple[int, int, int]]) -> list[int]:
    # kruskals
    # TODO: make forest heapq
    mins = [0] * n
    mst = set()
    forest = []
    for leaf in range(n):
        forest.append({leaf})

    waterways.sort(key=lambda tup: tup[2], reverse=True)
    for way in waterways:
        tree0 = find(forest, way[0])
        tree1 = find(forest, way[1])

        if tree0 is not tree1:
            mst.add(way)
            res = tree0.union(tree1)
            forest.append(res)
            forest.remove(tree0)
            forest.remove(tree1)

    print("-----------------------------")
    print(mst)

    # bfs to each vertex and return min edge to each vertex
    return mins


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
    
