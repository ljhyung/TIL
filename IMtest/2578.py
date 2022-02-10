
def bingo(lst):
    total = 0
    for i in range(5):
        if sum(lst[i]) == 5:
            return True
    for j in range(5):
        if sum(list(zip(lst[0], lst[1], lst[2], lst[3], lst[4]))[j]) == 5:
            return True
    for k in range(5):
        total += lst[k][k]
    if total == 5:
        return True
    total = 0
    for l in range(5):
        total += lst[4-l][l]
    if total == 5:
        return True
    return False

lst = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
]

chel_dict = {}
for i in range(5):
    chel_list = list(map(int, input().split()))
    for j in range(5):
        chel_dict[chel_list[j]] = 0

for i in range(5):
    hesul_list = list(map(int, input().split()))

