def sucessor_grid(x, y, dx, dy, mapa):
    vizinhos = []
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for mov in movimentos:
        novo_x = x + mov[0] * dx
        novo_y = y + mov[1] * dy
        if 0 <= novo_x < len(mapa) and 0 <= novo_y < len(mapa[0]) and mapa[novo_x][novo_y] == 0:
            vizinhos.append((novo_x, novo_y))
    return vizinhos
