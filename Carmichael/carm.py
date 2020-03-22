import sys
import math

carmichaels = [False]*65000

#Precomputar primos con la criba de erastotenes
def sieve(xs):
    return [] if not xs else xs[:1] + sieve([x for x in xs[1:] if x % xs[0] > 0])

def iscarmichael(x):
    if primos[x]:
        return False
    for a in range(2, x):
        if pow(a, x, x) != a:
            return False
    return True

primos = sieve(range(2,65000))

for i in range(65000):
    carmichaels[i] = iscarmichael(i)

if __name__ == "__main__":
    while True:
        num = int(sys.stdin.readline().strip())
        if num == 0:
            break
        if carmichaels[num]:
            print('The number '+str(num)+' is a Carmichael number.')
        else:
            print(str(num)+' is normal.')    