# Uses python3
def calc_fib(n):
    pre_set_array = [0,1]
    for i in range(2,n+1):
        pre_set_array.append(pre_set_array[i-2]+pre_set_array[i-1])
    result = pre_set_array[n]
    return result

n = int(input())
print(calc_fib(n))
