# Uses python3
import sys
def merge(B,C):
    b =0
    c = 0
    result_list = []
    for i in range(0,len(B)+len(C)):
        if b<len(B) and c<len(C):
            if B[b]<C[c]:
                result_list.append(B[b])
                b+=1
            if B[b] == C[c]: # not necessary sort b, just for good-looking
                if B[b][1]<=C[c][1]:
                    result_list.append(B[b])
                    b += 1
                else:
                    result_list.append(C[c])
                    c += 1
            else:
                result_list.append(C[c])
                c+=1
        elif b<len(B):
            result_list.append(B[b])
            b+=1
        elif c<len(C):
            result_list.append(C[c])
            c+=1
    return  result_list

def merge_sort(A):
    if len(A)<=1:
        return A
    mid_point = len(A)//2
    B = A[0:mid_point]
    C = A[mid_point:]
    list1 = merge_sort(B)
    list2 = merge_sort(C)
    list3 = merge(list1,list2)
    return list3

def binery_search(A,x):
    l = 0
    r = len(A)
    if A[l]>x:
        return -1
    if A[r-1]<x:
        return r

    while r-l>=2:
        mid_point = (r+l)//2
        if A[mid_point]==x:
            return mid_point
        elif A[mid_point]>x:
            r = mid_point
        elif A[mid_point]<x:
            l = mid_point
    if A[l]==x:
        return l
    elif A[r]==x:
        return r
    else:
        return l


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    st_ends = []
    sorted_st_ends = []
    for i in range(0,len(starts)):
        ele = [starts[i],ends[i]]
        st_ends.append(ele)
    sorted_st_ends = merge_sort(st_ends)
    sorted_starts = []
    for i in range(0,len(starts)):
        sorted_starts.append(sorted_st_ends[i][0])

    for i in range(0,len(points)):
        sorted_ends = []
        temp_list = sorted_st_ends
        m1 = binery_search(sorted_starts,points[i])
        temp_list = temp_list[m1:]
        for i in range(0,len(temp_list)):
            sorted_ends.append(sorted_st_ends[i][1])
        m2 = binery_search(sorted_ends,points[i])
        temp_list = temp_list[:m2]
        cnt[i]=len(temp_list)
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

