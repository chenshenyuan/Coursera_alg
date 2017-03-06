# Uses python3
import sys
# this method avoid the loop by %
# stty -echoctl
# without setting coin cost as int, it would be float
def get_change(m):
    coin_cost = 0
    if m >=10:
        residul = m%10
        coin_cost = int ((m-residul)/10) + coin_cost
        m = residul

    if m >=5:
        residul = m%5
        coin_cost = int ((m-residul)/5) + coin_cost
        m = residul
    if m >=1:
        coin_cost = coin_cost + m


    return coin_cost

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
