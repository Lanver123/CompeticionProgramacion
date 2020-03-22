primos = [-1]*20
def eratosthenes(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            primos[i] = i
            for j in range(i*i, n+1, i):
                multiples.append(j)
    return primos

print(eratosthenes(20))