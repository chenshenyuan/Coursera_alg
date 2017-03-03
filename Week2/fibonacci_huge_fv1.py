# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
# look for 01 sequence for Pisano period

    period_fre = 0
    former = 0
    current = 1
    fib_mod_list = [0,1] # list of mod for each fib numb
    period_fre_list = [0]
    for i in range(2,n+1):
        append_numb = former + current #Fn
        former = current
        current = append_numb
        append_numb2 = append_numb%m
        fib_mod_list.append(append_numb2)

        if (append_numb2 == 1 and fib_mod_list[i-1]==0): # if there is a 01 sequence
            period_fre_list.append(i-1) # locate the 01 sequence
            if len(period_fre_list) >= 2: # if there is one 01 sequence
                period_fre = period_fre_list[1]-period_fre_list[0] #period
                #print("yes") # if there is a period, print yes, sometimes there is no period
                break # finde the frequence
    #print(period_fre_list)
    #print(n,period_fre)

    if period_fre != 0:
        magic_numb = n%period_fre
        return fib_mod_list[magic_numb]
    else:
        return fib_mod_list[n] # if there is no period, then just return the last one





if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

#n = int(input())
#m = int(input())
#n = 2816213588
#m = 30524
#print(get_fibonacci_huge_naive(n, m))