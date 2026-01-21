from math import sqrt

def sucessores(atual, mapa, dim_x, dim_y):
    f = []
    x = atual[0]
    y = atual[1]
    
    if y + 1 != dim_y and mapa[x][y + 1] == 0:
        f.append([x, y + 1, 1])
    if x + 1 != dim_x and mapa[x + 1][y] == 0:
        f.append([x + 1, y, 3])
    if x - 1 >= 0 and mapa[x - 1][y] == 0:
        f.append([x - 1, y, 2])
    if y - 1 >= 0 and mapa[x][y - 1] == 0:
        f.append([x, y - 1, 4])
    return f

def Gera_Ambiente(arquivo):
    with open(arquivo, "r") as f:
        mapa = [list(map(int, linha.strip().split(","))) for linha in f]
    return mapa, len(mapa), len(mapa[0])

def h(p1, p2):
    m1 = 3 if p1[0] < p2[0] else 2
    m2 = 1 if p1[1] < p2[1] else 4
    return abs(p1[0] - p2[0]) * m1 + abs(p1[1] - p2[1]) * m2
