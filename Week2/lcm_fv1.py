# Uses python3
import sys
def gcd_advanced(a, b):

    while (a*b) !=0:
#        print(a,b)
        if a==b:
            return a
        elif a>b:
            a = a%b
        elif a<b:
            b = b%a
    if a ==0:
        return b
    else:
        return a

def lcm_naive(a, b):
    gcd_numb = gcd_advanced(a,b)
    return  int (a*b/gcd_numb)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

