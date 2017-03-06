# Uses python3
import sys
# find the maximu value per unit first and then use one by one
def get_optimal_value(capacity, weights, values):
    value = 0.
    total_numb = len(weights)
    value_per_unit = []
    for i in range(total_numb):
        value_per_unit.append(values[i]/weights[i])
    while capacity>0:
        max_v_p_u = max(value_per_unit)
        max_i = value_per_unit.index(max_v_p_u)
        amount_use = min(weights[max_i],capacity)
        value = amount_use*max_v_p_u + value
        capacity = capacity - amount_use
        value_per_unit[max_i] = 0
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
