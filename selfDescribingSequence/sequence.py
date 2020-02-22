from bisect import bisect_left  # Binary search
import sys

# Precalculus
res = [0, 1, 3]
i = 3
while res[-1] <= 2e9:
    res.append(res[i - 1] + bisect_left(res, i))
    i += 1


def golomb(n):
    return bisect_left(res, n)


if __name__ == '__main__':
    output = ''
    n = int(input())

    while n != 0:
        fn = golomb(n)
        print(fn)
        n = int(input())