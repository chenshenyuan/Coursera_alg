# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    list_of_last_digit = [0,1]
    sum_of_fn = 1
    for i in range(2,n+1):
        last_digit_of_fn = (list_of_last_digit[i-1]+list_of_last_digit[i-2])%10
        list_of_last_digit.append(last_digit_of_fn)
        sum_of_fn = (sum_of_fn+last_digit_of_fn)%10


    return sum_of_fn

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
