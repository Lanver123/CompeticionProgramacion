import sys

def calculateOnes(n):
    x = n
    counter = 0
    
    while x > 0: 
        while x % 10 == 1:
            counter += 1
            x //= 10
        if x > 0:
            x += n
    return counter

if __name__ == '__main__':

    while True:
        try:
            line = None
            line = input()
        except:
            pass
        if line is None: break
        
        n = int(line)
        ones = calculateOnes(n)
        print(ones)