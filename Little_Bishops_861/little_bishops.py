from collections import deque
from pprint import pprint
# Tip del profesor:
#   Generar todas las soluciones para n,k : 1 <= n <= 8, 0 <= k <= n*n

# Solucion para k piezas en tablero(n,n)
# Soluciones tipo ( (1,1),(1,2),(1,3)(1,4),(2,1)... )
SOLUTIONS = {}

def factible(pos, current_sol):
    return 0

# Genera una lista de posiciones posibles por diagonal:
# [[Diagonal1][Diagonal2][Diagonal3]...]
# Arriba a la izquierda es (1,1)
# Abajo a la derecha es (n,n)
def posiciones_posibles(n, k):
    result = deque()

    # Fila de arriba hasta (n-1)
    for diag in range(1, n):
        pos = (diag,1)
        aux_queue = deque()
        for _ in range(1, n-diag+2):
            aux_queue.append(pos)
            pos = (pos[0]+1,pos[1]+1)
        result.append(aux_queue)

    # Esquina arriba derecha / abajo izquierda
    pos1 = (n, 1)
    pos2 = (1, n)
    result.append(deque([pos1, pos2]))

    # Columna izquierda
    for diag in range(2, n):
        pos = (1,diag)
        aux_queue = deque()
        for _ in range(1, n-diag+2):
            aux_queue.append(pos)
            pos = (pos[0]+1,pos[1]+1)
        result.append(aux_queue)

    return result

def solution(n, k):
    solutions = deque()

if __name__ == "__main__":
    pprint(posiciones_posibles(3,2))
    #for n in range(1, 9):
    #    for k in range(0, n*n+1):
    #        pass
