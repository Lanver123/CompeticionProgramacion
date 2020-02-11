import sys

nPeopleLeft = 0
result = ''
totalResult = ''
totalTime = 0

def countingSort(array):
    minElement = min(array)
    maxElement = max(array)
    difference = maxElement - minElement + 1
    arrayGrande = [0] * difference
    result = list()

    for x in array:
        arrayGrande[x - minElement] += 1 
    
    for index,elem in enumerate(arrayGrande):
        while elem > 0:
            result.append(index + minElement)
            elem -= 1
    return result

def crossGeneralPeople():
    global totalTime
    global nPeopleLeft
    global result

    optionA = speedPassengers[0] + 2 * speedPassengers[1] + speedPassengers[nPeopleLeft - 1]
    optionB = 2 * speedPassengers[0] + speedPassengers[nPeopleLeft - 2] + speedPassengers[nPeopleLeft - 1]

    if optionA < optionB:
        totalTime += optionA
        result += str(speedPassengers[0]) + " " + str(speedPassengers[1]) + "\n"
        result += str(speedPassengers[0]) + "\n"
        result += str(speedPassengers[nPeopleLeft - 2]) + " " + str(speedPassengers[nPeopleLeft - 1]) + "\n"
        result += str(speedPassengers[1]) + "\n"
    else:
        totalTime += optionB
        result += str(speedPassengers[0]) + " " + str(speedPassengers[nPeopleLeft - 2]) + "\n"
        result += str(speedPassengers[0]) + "\n"
        result += str(speedPassengers[0]) + " " + str(speedPassengers[nPeopleLeft - 1]) + "\n"
        result += str(speedPassengers[0]) + "\n"
    
    nPeopleLeft -= 2

def left3People():
    global totalTime
    global nPeopleLeft
    global result

    time = speedPassengers[0] + speedPassengers[1] + speedPassengers[2]
    totalTime += time
    result += str(speedPassengers[0]) + " " + str(speedPassengers[1]) + "\n"
    result += str(speedPassengers[0]) + "\n"
    result += str(speedPassengers[0]) + " " + str(speedPassengers[2])

def left2People():
    global totalTime
    global nPeopleLeft
    global result

    time = speedPassengers[1]
    totalTime += time
    result += str(speedPassengers[0]) + " " + str(speedPassengers[1])

def left1People():
    global totalTime
    global nPeopleLeft
    global result

    time = speedPassengers[0]
    totalTime += time
    result += str(speedPassengers[0])

def crossBridge():
    global haveCross

    while nPeopleLeft >= 4:
        crossGeneralPeople()

    if nPeopleLeft == 3:
        left3People()
    elif nPeopleLeft == 2:
        left2People()
    elif nPeopleLeft == 1:
        left1People()


if __name__ == '__main__':

    nCases = int(input())
    while nCases > 0:
        totalTime = 0
        result = ''

        nCases -= 1
        line = ''

        while len(line) == 0:
            line = input().strip()
        nPassengers = int(line)
        speedPassengers = []

        for i in range(nPassengers):
            speedPassengers.append(int(input().strip()))
        
        nPeopleLeft = len(speedPassengers)
        speedPassengers = countingSort(speedPassengers)
        crossBridge()
        result = str(totalTime) + "\n" + result
        totalResult += result
        
        if nCases > 0:
            totalResult += "\n\n"
    print(totalResult)