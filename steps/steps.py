import sys
import math as m

def calculateSteps(x,y):
    distance = y - x
    if distance != 0:
        step = int(m.sqrt(distance))
        if step * step == distance:
            step = step * 2 - 1
        elif step * step + step < distance:
            step = step * 2 + 1
        else:
            step = step * 2
    else:
        step = 0
    return step


if __name__ == '__main__':
    nCases = int(input())

    i = 0
    res = ''
    while i < nCases:
        line = input().split()
        x = int(line[0])
        y = int(line[1])
        res += str(calculateSteps(x,y))
        if i < nCases - 1:
            res += '\n'
        i += 1
    print(res)