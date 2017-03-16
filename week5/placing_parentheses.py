# Uses python3
import math
def evalt1(a, b, op):
    if op == '+':
        return (a + b)
    elif op == '-':
        return (a - b)
    elif op == '*':
        return (a * b)
    else:
        assert False

def get_maximum_value(dataset1):
    dataset2 = list(dataset1)
    n = (len(dataset2)-1)//2+1
    dataset = []
    for i in range(0,len(dataset2)):
        if i%2 ==0:
            ele = int(dataset2[i])
            dataset.append(ele)
        else:
            dataset.append(dataset2[i])
    m_min = []
    M_max = []
    for i in range(0,n):
        m_min.append([0]*(n))
        M_max.append([0]*(n))
        m_min[i][i]= dataset[2*i]
        M_max[i][i]= dataset[2*i]
    for s in range(1,n):
        for i in range(0,n-s):
            j = i+s
            min_numb = math.inf
            max_numb = -math.inf
            for k in range(i,j):
                op = dataset[2*k+1]
                a = evalt1(M_max[i][k],M_max[k+1][j],op)
                b = evalt1(M_max[i][k],m_min[k+1][j],op)
                c = evalt1(m_min[i][k],M_max[k+1][j],op)
                d = evalt1(m_min[i][k],m_min[k+1][j],op)
                min_numb = min(min_numb,a,b,c,d)
                max_numb = max(max_numb,a,b,c,d)
            M_max[i][j] = max_numb
            m_min[i][j] = min_numb

    return M_max[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
