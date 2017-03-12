# Uses python3
import sys
import math
'''
rather than iteration, we should use loop since left and right are stated each time it's called
'''
def binary_search(a, x):
    left, right = 0, len(a)
    while right>left:
        mid_point = math.floor((left+right)/2)
        if a[mid_point] ==x:
            return mid_point
        if a[mid_point]>x:
            right = mid_point-1
        else:
            left = mid_point+1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')
'''
a = [1,5,8,12,13]
b = [8,1,23,1,11]
for x in b:
    c = linear_search(a,x)
    d = binary_search(a,x)
    #print(c,end=' ')
    print(d,end = ' ')
'''