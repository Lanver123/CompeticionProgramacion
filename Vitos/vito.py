import sys
num_cases = int(sys.stdin.readline())

for _ in range(num_cases):
    #Vito vive en la mediana de las casas
    #despues solo queda sumar el valor absoluto
    casas = [int(i) for i in sys.stdin.readline().split()[1:]]
    mediana = sorted(casas)[int(len(casas)/2)]
    cont = sum([abs(elem-mediana) for elem in casas])
    print(cont)