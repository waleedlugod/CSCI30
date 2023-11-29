#!/usr/bin/env python3
def widest_barge(n: int, waterways: list[tuple[int, int, int]]) -> list[int]:
    '''
    Given the number of locations `n` and a list of waterways, return a list
    of n-1 integers where the ith integer denotes the width of the largest
    possible barge that can safely travel from location 0 to location i.
    '''
    # kruskals
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
    
