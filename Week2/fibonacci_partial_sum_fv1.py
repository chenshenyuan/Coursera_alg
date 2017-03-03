# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1
    if from_<=1:
        sum_last_digit = 1
    else:
        sum_last_digit = 0

    for i in range(2,to+1):
        previous, current = current, (previous + current)%10

        if i >= from_:
            sum_last_digit = (sum_last_digit + current)%10


    return sum_last_digit


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
