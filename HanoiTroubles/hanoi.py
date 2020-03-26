import sys
ncasos = int(sys.stdin.readline())

# Para solucionar este problema el aproach ha sido precomputar todas las soluciones posibles
# en un programa a parte.

soluciones = [1, 3, 7, 11, 17, 23, 31, 39, 49, 59, 71, 83, 97, 111, 127, 143, 161, 179, 199, 
219, 241, 263, 287, 311, 337, 363, 391, 419, 449, 479, 511, 543, 577, 611, 647, 683, 721, 
759, 799, 839, 881, 923, 967, 1011, 1057, 1103, 1151, 1199, 1249, 1299]

for _ in range(ncasos):
    number = int(sys.stdin.readline())
    print(soluciones[number-1])