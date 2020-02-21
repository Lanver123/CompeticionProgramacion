import sys
factorialFactors = {}

def primeFactors(n):
    i = 2
    global factorialFactors
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            k = factorialFactors.get(i,0) + 1
            factorialFactors[i] = k
    if n > 1:
        k = factorialFactors.get(n,0) + 1
        factorialFactors[n] = k
    return factorialFactors

def output(fact,div,divides):
    res = str(div) + ' '
    if divides:
        res += 'divides '
    else:
        res += 'does not divide '
    res += str(fact) +'!'
    print(res)

def doesDivisor(n, div):
    for p in div.keys():
        e = div.get(p)
        i = 2
        while i < n + 1 and e > 0:
            x = i
            while e > 0 and x % p == 0:
                e -= 1
                x /= p
            i += 1
        if e > 0:
            return False
    return True

if __name__ == '__main__':
    while True:
        try:
            line = None
            line = input()
        except:
            pass
        
        if line is None: break
        line = line.strip()
        if len(line) == 0: break
        
        line = line.split()

        factorialFactors = {}
        factorial = int(line[0])
        divisor = int(line[1])

        divisorFactors = primeFactors(divisor)
        
        doesDivide = doesDivisor(factorial, divisorFactors)
        output(factorial,divisor,doesDivide)