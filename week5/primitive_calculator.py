# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def Get_C(C,n):
    result = []
    while n>1:
        result.append(n)
        c_min = C[n-2]
        n_min = n-1
        if n%2 ==0 and C[(n//2)-1]<= c_min:
            c_min = C[(n//2)-1]
            n_min = n//2
        if n%3 ==0 and C[(n//3)-1]<= c_min:
            c_min = C[(n//3)-1]
            n_min = n//3
        n = n_min
    result.append(1)
    return result

def optimal_sequence2(n):

    C = [0]*(n+3)
    C[0] = 0  # 1
    C[1] = 1  # 2
    C[2] = 1  # 3
    for i in range(4,n+1):
        c1 = C[i-2]+1
        result = c1
        if i % 3 == 0:
            c2 = C[(i//3)-1]+1
            if c2<=result:
                result = c2
        if i % 2 == 0:
            c3 = C[(i//2)-1]+1
            if c3<=result:
                result = c3
        C[i-1] = result

    sequence = Get_C(C,n)
    return reversed(sequence)





input = sys.stdin.read()
n = int(input)

sequence = list(optimal_sequence2(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
