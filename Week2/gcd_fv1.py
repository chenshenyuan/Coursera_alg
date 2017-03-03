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



if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_advanced(a, b))

#a = int (input())
#b = int (input())
#print(gcd_advanced(a, b))

