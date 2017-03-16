#Uses python3

import sys


def edit_distance(s, t):
    m = len(s)  # numb of row
    n = len(t)  # numb of col
    D = []
    for i in range(0, m + 1):
        D.append([0] * (n + 1))
    for i in range(1, m + 1):
        D[i][0] = i
    for i in range(1, n + 1):
        D[0][i] = i
    D[m][n] = 0
    # build matrix and initial
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            i1 = D[i][j - 1] + 1
            d1 = D[i - 1][j] + 1
            mat1 = D[i - 1][j - 1]
            Mism1 = D[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                D[i][j] = min(i1, d1, mat1)
            else:
                D[i][j] = min(i1, d1, Mism1)
    return D

def lcs2(a, b):
    m = len(a)
    n = len(b)
    D = edit_distance(a, b)
    output = []
    while m > 0 or n > 0:
        if m > 0 and D[m][n] == D[m - 1][n] + 1:
            m = m - 1
        elif n > 0 and D[m][n] == D[m][n - 1] + 1:
            n = n - 1
        elif m > 0 and n > 0 and D[m][n] == D[m - 1][n - 1]:
            output.append(a[m - 1])
            m = m - 1
            n = n - 1
        else:
            m = m - 1
            n = n - 1
    output.reverse()
    return output

def lcs3(a, b, c):
    d = lcs2(a,b)
    output = lcs2(d,c)
    return len(output)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
