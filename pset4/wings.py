#!/usr/bin/env python3

def arrange_wings(wings, obs):
    '''
    Given the list of wings `wings` and observations `obs`, return *any*
    possible ordering of the wings (as a list) as determined by the observations,
    or `None` if no such ordering is possible.
    '''
    # TODO: topo sort
    raise NotImplementedError


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
