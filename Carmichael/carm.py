import sys
import math
import itertools as it

primos = [False] * 65000
carmichaels = [False]*65000

def erat3( ):
    D = { 9: 3, 25: 5 }
    yield 2
    yield 3
    yield 5
    MASK= 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS= frozenset( (1, 7, 11, 13, 17, 19, 23, 29) )

    for q in it.compress(
            it.islice(it.count(7), 0, None, 2),
            it.cycle(MASK)):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = q + 2*p
            while x in D or (x%30) not in MODULOS:
                x += 2*p
            D[x] = p


for prime in erat3():
    if prime > 65000:
        break
    primos[prime] = True

def iscarmichael(x):
    if primos[x]:
        return False
    for a in range(2, x):
        if pow(a, x, x) != a:
            return False
    return True

for i in range(2, 65000):
    carmichaels[i] = iscarmichael(i)

while True:
    num = int(sys.stdin.readline().strip())
    if num == 0:
        break
    if carmichaels[num]:
        print('The number '+str(num)+' is a Carmichael number.')
    else:
        print(str(num)+' is normal.')