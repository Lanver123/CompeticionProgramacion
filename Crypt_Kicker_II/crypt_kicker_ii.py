# Permute letters, no two letters are replaced by the same Esto no => {a -> b, c -> b}
# Alguna de las lineas siempre será "the quick brown fox jumps over the lazy dog"

#       1
#       vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq
#       xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj
#       frtjrpgguvj otvxmdxd prm iev prmvx xnmq


target = "the quick brown fox jumps over the lazy dog".split(" ")

numcases = int(input())
input() # blank line
for case in range(numcases):
    letras = {}
    lines = []
    while True:
        try:
            line = input()
        except:
            break
        if line == "":
            break
        lines += [line.split(" ")]

# Encontrar el primer match con los tamaños de las palabras del target
#   -> rellenar el abecedario con las correspondencias
# Empezar desde la linea 0 traduciendo
#   -> si encuentras una letra sin correspondencia. error

    #Buscar target
    encontrado = False
    for line in lines:
        if len(line) != len(target):
            continue
        
        i = 0
        while i < len(line):
            if len(target[i]) != len(line[i]):
                break
            i+=1
        
        # Encontrada coincidencia
        if i == len(line):
            for index1, word in enumerate(line):
                for index2, letra in enumerate(word):
                    letras[letra] = target[index1][index2]
            
            if(len(list(letras.values())) == len(set(letras.values()))):
                encontrado = True
                break

    #Con el target encontrado, traducir
    if len(letras.keys()) != 26 or not encontrado:
        print("No solution.")
    else:
        for line in lines:
            print_line = ""
            for word in line: 
                for letra in word:
                    print_line += letras[letra]
                print_line += " " 
            print(print_line.strip())
    
    print()


