#Uses python3
import sys
import math

def minimum_distance(x, y):
    if len(x)==2 or len(x)==3:
        return math.sqrt(math.pow(x[1]-x[0],2)+math.pow(y[1]-y[0],2))
    if len(x)<=1:
        return -1
    sorted_x = sorted(x)
    median_numb = sorted_x[len(x)//2]
    list1_x = []
    list1_y = []
    list2_x = []
    list2_y = []
    for i in range(0,len(x)):
        if x[i]>median_numb:
            list1_x.append(x[i])
            list1_y.append(y[i])
        elif x[i]>median_numb:
            list2_x.append(x[i])
            list2_y.append(y[i])

    d1 = minimum_distance(list1_x,list1_y)
    d2 = minimum_distance(list2_x,list2_y)

    result_list = []
    if d1>= 0:
        result_list.append(d1)
    if d2>=0:
        result_list.append(d2)
    if len(result_list)==0:
        d3 = d3_generator(x, y)
        return d3
    result_min = min(result_list)
    list3_x = []
    list3_y = []
    for i in range(0,len(x)):
        if abs(x[i]-median_numb)<=result_min:
            list3_x.append(x[i])
            list3_y.append(y[i])
    d3 = d3_generator(list3_x,list3_y)
    if d3>=0 and d3<result_min:
        result_min = d3

    return result_min
def d3_generator(x,y):
    if len(x)<=1:
        return -1
    if len(x)==2:
        return math.sqrt(math.pow(x[1] - x[0], 2) + math.pow(y[1] - y[0], 2))
    result_list = []
    for i in range(0,len(x)):
        for k in range(i+1,len(x)):
            d3 = math.sqrt(math.pow(x[i] - x[k], 2) + math.pow(y[i] - y[k], 2))
            result_list.append(d3)

    min_d3 = min(result_list)
    return min_d3

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
