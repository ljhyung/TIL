import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):
    st = '('
    end = ')'
    lst = list(input())

    result = 0
    raser = 0
    rasercheck = False
    other = 0
    for j in range(len(lst)):       # 처음 했던 방법 레이저를 ()연속으로 판별하는데 변수를 따로 썼다
        if lst[j] == st:
            other += 1
            rasercheck = True
        elif lst[j] == end and rasercheck:
            other -= 1
            raser += 1
            rasercheck = False
        elif lst[j] == end:
            other -= 1
            result += 1
        if raser:
            result += other
            raser -= 1
    # for j in range(len(lst)):
    #     if lst[j] == st:
    #         other += 1
    #     else:
    #         other -= 1
    #         if lst[j-1] == st:    # 이전 값을 판단해 레이저를 판별
    #             result += other
    #         else:
    #             result += 1

    print(f'#{tc+1} {result}')
