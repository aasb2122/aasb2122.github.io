def score(x1, x2):
    return 2 if x1 == x2 else -1

def pmat(s1, s2, mat):
    print(" ", *("-" + s2), sep = " " * 3)
    for x1, linha in zip("-" + s1, mat):
        print(x1, *[f"{x : 3d}" for x in linha])

def ptr(s1, s2, mat):
    print(" ", *("-" + s2), sep = " " * 3)
    for x1, linha in zip("-" + s1, mat):
        print(x1, *[x.rjust(3) for x in linha])

        
def align(s1, s2, g = -1):
    mat = [[0 for C in range(len(s2) + 1)] for L in range(len(s1) + 1)]
    tr = [[" " for C in range(len(s2) + 1)] for L in range(len(s1) + 1)]

    for L in range(len(s1)):
        mat[L + 1][0] = mat[L][0] - 1
        tr[L + 1][0] = "C"
    for C in range(len(s2)):
        mat[0][C + 1] = mat[0][C] - 1
        tr[0][C + 1] = "E"
        
    for L, x1 in enumerate(s1):
        for C, x2 in enumerate(s2):
            valor = [
                mat[L][C] + score(x1, x2),  # diagonal
                mat[L + 1][C    ] + g,      # vertical
                mat[L    ][C + 1] + g]      # horizontal
            direcoes = "D E C".split()
            mat[L + 1][C + 1] = max(*valor)
            tr[L + 1][C + 1] = direcoes[valor.index(mat[L + 1][C + 1])]
    """
    pmat(s1, s2, mat)
    print()
    ptr(s1, s2, tr)
    """
    
    L = len(s1)
    C = len(s2)
    S1, S2 = "", ""
    while L > 0 or C > 0:
        dir = {'D': (-1, -1), 'E' : (0, -1), 'C' : (-1, 0)}
        DL, DC = dir[tr[L][C]]
        L += DL
        C += DC
        if tr[L][C] == "D":
            S1 = s1[L - 1] + S1
            S2 = s2[C - 1] + S2
        if tr[L][C] == "E":
            S1 = "-" + S1
            S2 = s2[C - 1] + S2            
        if tr[L][C] == "C":
            S1 = s1[L - 1] + S1
            S2 = "-" + S2
    #print(S1, S2, sep = "\n")

    return mat[len(s1)][len(s2)], S1, S2
    

print(align("ATGAAGGT", "AGAGAGGC"))
