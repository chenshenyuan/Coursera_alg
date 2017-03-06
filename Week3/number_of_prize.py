# Uses python3
import sys

def optimal_summands(n):
    summands = []
    while n>0:
        if len(summands) == 0:
            add_numb = 1
        else:
            add_numb = summands[-1]+1

        if add_numb*2>=n: #only one answer that is n which is the left space
            add_numb = n #set add_numb as the left
            summands.append(add_numb)
            n = n-add_numb
        else: # it is safe to use add_numb
            summands.append(add_numb)
            n = n - add_numb
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

'''
the greedy alg use here is every times add 1 to the last number
the space get less and the initial number get bigger until one time
the double of initial number is larger than the left space (money left)
then, the last prize own all of the left money

'''