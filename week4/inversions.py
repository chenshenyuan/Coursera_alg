# Uses python3

import sys
import math

def Merge(a,b,left,right):
    mix_list = []
    count = 0
    if right-left <=1:
        if b[left]>b[right]:
            count+=1
            mix_list.append(b[left])
            mix_list.append(b[right])
        else:
            mix_list.append(b[left])
            mix_list.append(b[right])
    else:
        mid_point = (right+left)//2
        B = b[left:mid_point]
        C = b[mid_point:right]

        n = len(B)+len(C)
        b1 = 0
        c1 = 0
        while b1< len(B) and c1<len(C):
            if B[b1]<= C[c1]:
                mix_list.append(B[b1])
                b1+=1
            elif B[b1]> C[c1]:
                count+=1
                mix_list.append(C[c1])
                c1+=1
        if b1<len(B):
            for i in B[b1:]:
                mix_list.append(i)
        else:
            for i in C[c1:]:
                mix_list.append(i)
    for i in range(0,len(mix_list)):
        b[left+i]=mix_list[i]

    return count

def MergeSort(A):
    if len(A) ==1:
        return A[0]
    mid_point = math.floor(len(A)/2)
    B = MergeSort(A[0:mid_point])
    C = MergeSort(A[mid_point+1:len(A)])
    A_result = Merge(B,C)
    A_new = A_result[:-1]
    return A_new



def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        b[left] = a[left]
        return number_of_inversions

    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions+= Merge(a,b,left,right)

    return number_of_inversions



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))






