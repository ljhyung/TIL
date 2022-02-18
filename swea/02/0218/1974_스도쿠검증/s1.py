import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def check_row(lst):
    for i in range(9):
        check = [0 for _ in range(10)]
        for j in lst[i]:
            check[j] += 1
        if 0 in check[1:]:
            return 0
    return 1

def check_sq(lst):
    for i in range(0,9,3):
        for j in range(0,9,3):
            check = [0 for _ in range(10)]
            for k in range(3):
                for l in range(3):
                    check[lst[i+k][j+l]] += 1
            if 0 in check[1:]:
                return 0
    return 1

for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(9)]
    a = check_row(lst)
    for i in range(9):
        for j in range(9):
            if i>j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    b = check_row(lst)
    c = check_sq(lst)
    d = bool(a and b and c)
    print(f'#{tc} {int(d)}')


