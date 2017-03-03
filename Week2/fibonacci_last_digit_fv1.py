# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    fn_list = [0,1]

    for i in range(2,n+1):
        add_numb = (fn_list[i-1]+fn_list[i-2])%10
        fn_list.append(add_numb)

    return fn_list[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
