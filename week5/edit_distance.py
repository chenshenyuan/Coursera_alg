# Uses python3
def edit_distance(s, t):
    m = len(s) #numb of row
    n = len(t) #numb of col
    D = []
    for i in range(0, m + 1):
        D.append([0] * (n + 1))
    for i in range(1, m + 1):
        D[i][0] = i
    for i in range(1, n + 1):
        D[0][i] = i
    D[m][n] = 0
    # build matrix and initial
    for j in range(1, n+1):
        for i in range(1, m+1):
            i1 = D[i][j - 1] + 1
            d1 = D[i - 1][j] + 1
            mat1 = D[i - 1][j - 1]
            Mism1 = D[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                D[i][j] = min(i1, d1, mat1)
            else:
                D[i][j] = min(i1, d1, Mism1)
    return D[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
