#Uses python3
import sys

def largest_number(a):
    numb_of_ele = len(a)
    b = []
    while len(b)< numb_of_ele:
        max_digit = '0'
        for i in a:
            if ISGREATER(i,max_digit):
                max_digit = i
        b.append(max_digit)
        max_digit_index = a.index(max_digit)
        a.remove(a[max_digit_index])

    res = ""
    for x in b:
        res += x
    return res

def ISGREATER(digit ,maxdigit):
    dig_rep = digit+maxdigit
    dig_rep = int(dig_rep)
    max_dig_rep = int(maxdigit+digit)
    max_dig_rep = int(max_dig_rep)
    if dig_rep>max_dig_rep:
        return True
    else:
        return False



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
'''
a very important thing of this program is the input are treated as str instead of int
ISGREATER use the convertion between str and int.str make the number easy to compare
'''