a, b, c = map(int, input().split())

def profit(a, b, c):
    if b == c:
        return -1
    elif 0 > (a / (c - b)):
        return -1
    else:
        return int(a / (c - b)) +1


print(profit(a, b, c))