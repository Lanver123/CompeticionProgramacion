import sys
import math


primos = [False] * 65000
carmichaels = [False]*65000


def iscarmichael(x):
    if primos[x]:
        return False
    for a in range(2, x):
        if pow(a, x, x) != a:
            return False
    return True

#Precomputar primos hasta 65000
for i in range(2, 65000):
    if all(i%j!=0 for j in range(2,int(math.sqrt(i))+1)):
       primos[i] = True

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