# Uses python3
import sys

def optimal_weight(W, w):
    if len(w) <=1:
        if w[0]<=W:
            return w[0]
        else:
            return 0
    else:
        v1 = w[0]
        w_next = w[1:]
        result1 = optimal_weight(W-v1,w_next)+v1
        result2 = optimal_weight(W,w_next)
        result = max(result1,result2)
        return result


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
