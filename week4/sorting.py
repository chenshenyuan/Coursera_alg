# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l+1,r+1):
        if a[i]==x:
            m1+=1
            m2+=1
            a[i],a[m1]= a[m1],a[i]
            a[m2],a[i] = a[i],a[m2]
        if a[i]<x:
            m2+=1
            a[m2],a[i] = a[i],a[m2]
    for i in range(0,m1+1):
        a[i],a[m2-m1+i] = a[m2-m1+i],a[i]
    return [m1,m2]


    pass

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    m = partition3(a,l,r)
    m1 = m[0]
    m2 = m[1]
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')


