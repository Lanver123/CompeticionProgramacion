import sys


def shellShort(original, target):
    moveTo = [0] * len(original)

    # guardar la posicion que tienen en el ordenado
    posTarget = {}

    for i in range(len(target)):
        turtle = target[i]
        posTarget[turtle] = i

    res = []
    j = 0
    # recorrerlo desde abajo
    for i in reversed(range(len(original))):
        turtleOrig = original[i]
        posTurtleTarget = posTarget.get(turtleOrig)
        if i != posTurtleTarget - j:
            j += 1
            res.append(posTurtleTarget)

    # en este punto se tienen los indices a mover de la lista final.
    # falta ordenarlos en orden descendente y sacar los nombres
    return [target[i] for i in sorted(res, reverse=True)]

if __name__ == '__main__':

    nCases = int(input())

    while nCases > 0:
        nCases -= 1
        line = ''

        while len(line) == 0:
            line = input().strip()
        nTurtles = int(line)

        originalOrder = []
        targetOrder = []

        # la posicion 0 es la primera de la pila
        for i in range(nTurtles):
            originalOrder.append(input().strip())
        
        for i in range(nTurtles):
            targetOrder.append(input().strip())
        
        res = shellShort(originalOrder, targetOrder)

        for turtle in res:
            print(turtle)

        print()