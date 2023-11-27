# f(n) = -1 + 2 - 3 + ... + n(-1)^n
#
# if n is even:
#   f(n) = (-1 + 2) + (-3 + 4) + ... + ((n-1)(-1)^(n-1) + n(-1)^n)  (pair up the numbers at indeces i and i + 1 where i is odd)
#        = (-1 + 2) + (-3 + 4) + ... + ((n-1)(-1) + n(1))           (since n is even and n - 1 is odd)
#        = 1 + 1 + 1 + ... + 1                                      (simplify)
#        = n / 2                                                    (n / 2 pairs)
#
# if n is odd:
#   f(n) = -1 + 2 - 3 + ... + (n-1)(-1)^(n-1) + n(-1)^n             (by definition)
#        = f(n - 1) + n(-1)^n                                       (by definition)
#        = f(n - 1) - n                                             (since n is odd)
#        = (n - 1) / 2 - n                                          (since n - 1 is even, substitute as defined above)
#        = (-n - 1) / 2                                             (simplify)
def deadsimplesum(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return (-n - 1) // 2
 
 
# DON'T TOUCH the code below
if __name__ == "__main__":
    n = int(input())
    print(deadsimplesum(n))
 
