def descending_order(num):
    return int(''.join([str(y) for y in sorted([int(i) for i in str(num)])[::-1]]))
