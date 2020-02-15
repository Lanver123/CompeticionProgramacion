from pprint import pprint
from collections import deque
# Not case sensitive -> pasarlo todo a minuscula

def print_grid(grid):
    for line in grid: print(line)

def build_hor_grid(pre_grid):
    horizontal_grid = []
    for row, line in enumerate(pre_grid):
        horizontal_grid += [[(c, row+1, col+1) for col, c in enumerate(line)]]
    return horizontal_grid            

def build_vert_grid(horizontal_grid):
    return [(list(line)) for line in zip(*horizontal_grid)]

def build_diag_grid1(grid):
    offset = [0]*(len(grid[0])-1)
    aux_grid = [offset + line for line in grid]
    diag_grid = []
    for i, line in enumerate(aux_grid):
        for _ in range(i):
            line.append(line.pop(0))
        diag_grid.append(line)

    diag_grid = [(list(line)) for line in zip(*diag_grid)]
    diag_grid = [[elem for elem in line if elem != 0] for line in diag_grid]
    return diag_grid

def build_diag_grid2(grid):
    offset = [0]*(len(grid[0])-1)
    aux_grid = [line+offset for line in grid]
    diag_grid = []
    for i, line in enumerate(aux_grid):
        for _ in range(i):
            line = [line.pop()] + line
        diag_grid.append(line)

    diag_grid = [(list(line)) for line in zip(*diag_grid)]
    diag_grid = [[elem for elem in line if elem != 0] for line in diag_grid]
    return diag_grid

def read_case():
    grid = [input().lower() for _ in range(int(input().split(" ")[0]))]
    targets = [input().lower() for _ in range(int(input()))]
    return grid, targets

def find_ocurrences(word, grid):
    for line in grid:
        cadena = "".join([c for c, row, col in line])
        if word in cadena:
            pos = cadena.index(word)
            yield line[pos]
        
        reversed_cadena = cadena[::-1]
        if word in reversed_cadena:
            pos = reversed_cadena.index(word)
            yield line[len(line)-pos-1]    
    

num_cases = int(input())
input()

for case in range(num_cases):    
    pre_grid, targets = read_case()
    try:
        input()
    except:
        pass    
    # Tupla (caracter, row, col)
    # Grid horizontal
    horizontal_grid = build_hor_grid(pre_grid)

    # Grid vertical
    vertical_grid = build_vert_grid(horizontal_grid)

    # Grid diagonal
    diag_grid1 = build_diag_grid1(horizontal_grid)
    diag_grid2 = build_diag_grid2(horizontal_grid)
    for target in targets:
        ocurrences = []
        ocurrences += [x for x in find_ocurrences(target, horizontal_grid)]
        ocurrences += [x for x in find_ocurrences(target, vertical_grid)]
        ocurrences += [x for x in find_ocurrences(target, diag_grid1)]
        ocurrences += [x for x in find_ocurrences(target, diag_grid2)]
        sorted_list = sorted(ocurrences, key=lambda elem: (elem[1], elem[2]))
        if len(sorted_list):
            print("%d %d" % (sorted_list[0][1], sorted_list[0][2]))
    if case < num_cases -1:
        print()
