# Uses python3
import sys
import math
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid_point = math.floor((left+right)/2)
    first_numb = get_majority_element(a,mid_point,right)
    second_numb = get_majority_element(a,left,mid_point)
    count1 = 0
    count2 = 0
    if first_numb !=-1:
        for i in a[left:right]:
            if i == first_numb:
                count1+=1
    if second_numb !=-1:
        for i in a[left:right]:
            if i==second_numb:
                count2 +=1
    if count1 > (right-left)/2:
        return first_numb
    if count2 > (right-left)/2:
        return second_numb

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

'''

a = [2,3,9,2,2]
b = len(a)
print(get_majority_element(a,0,b))
'''