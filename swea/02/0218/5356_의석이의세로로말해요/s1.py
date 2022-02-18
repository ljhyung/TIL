import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    lst = [input() for _ in range(5)]
    sol = []
    for j in range(15):
        for i in range(5):
            if len(lst[i]) > j:
                sol.append(lst[i][j])
    print(f'#{tc} {"".join(sol)}')