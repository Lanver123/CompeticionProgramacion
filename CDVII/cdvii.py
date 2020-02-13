if __name__ == "__main__":
    num_cases = int(input())
    input()  # blank line

    for case in range(num_cases):
        coches = {}
        tarifas = [int(tar) for tar in input().split(" ")]

        while True:
            try:
                line = input()
            except:
                break
            
            if(line == ""):
                break

            coche, hora, modo, punto = line.split(" ")
            if coche in coches.keys():
                coches[coche] += [(hora, modo, punto)]
            else:
                coches[coche] = [(hora, modo, punto)]

        coche_precio = {}
        for key, checkPoints in coches.items():
            ordenados = sorted(checkPoints, key=lambda tupla: tupla[0])
            precio = 0
            for i in range(len(ordenados)-1):
                if(ordenados[i][1]=="enter" and ordenados[i+1][1]=="exit"):
                    pareja = ordenados[i:i+2]
                    precio_km = tarifas[int(pareja[0][0][6:8])]/100
                    
                    distancia = abs(float(pareja[0][2]) - float(pareja[1][2]))
                    precio += 1.0 * precio_km * distancia + 1
            if(precio > 0):        
                coche_precio[key] = precio
            
        #queda ordenarlos
        keys = sorted(coche_precio.keys())
        for key in sorted(coche_precio.keys()):
            print("%s $%.2f" % (key, coche_precio[key]+2))
        
        if case < num_cases-1:
            print()
