import sys

# Permute letters, no two letters are replaced by the same Esto no => {a -> b, c -> b}
# Alguna de las lineas siempre será "the quick brown fox jumps over the lazy dog"

#       1
#       vtz ud xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq
#       xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj
#       frtjrpgguvj otvxmdxd prm iev prmvx xnmq


TARGET = "the quick brown fox jumps over the lazy dog"

ALFABETO = "abcdefghijklmnopqrstuvwxyz"
CONJUNTO_ALFABETO = set(ALFABETO)

def leer_input():
    lineas = []
    while True:
        linea = sys.stdin.readline()
        if linea == "" or linea == "\n":
            break
        else:
            lineas += [linea.strip()]
    return lineas

def traducir_linea(diccionario, linea):
    return "".join([diccionario[letra] for letra in linea])

def contiene_alfabeto(linea):
    return set(linea.replace(" ", "")) == CONJUNTO_ALFABETO

def mismo_tam_target(linea):
    if len(linea) != len(TARGET):
        return False
    
    if linea.count(" ") != TARGET.count(" "):
        return False
    
    for c1, c2 in zip(linea, TARGET):
        if c1 == " " and c2 != c1: return False

    return True

#### PROGRAMA

numcases = int(input())
input() # blank line

for case in range(numcases):
    lineas = leer_input()
    dicc = {}
    linea_fox = None
    #Busqueda target
    for linea in lineas:
        if not mismo_tam_target(linea):

            continue
        if not contiene_alfabeto(linea):
            continue
        linea_fox = linea
    
    if linea_fox is None:
        print("No solution.")
    else:
        for c1, c2 in zip(linea_fox, TARGET):
            dicc[c1] = c2

        for linea in lineas:
            print(traducir_linea(dicc, linea))

    if case < numcases-1:
        print()
        




    

            
