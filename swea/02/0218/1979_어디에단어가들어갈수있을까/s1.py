# import copy
import sys
sys.stdin = open("input.txt", "r")

def check(lst, N, K):
    # result = 0
    # for i in range(N+1):            # 마지막 0까지 검사해서 끝부분에 있을 때도 체크
    #     cnt = 0
    #     for k in range(N+1):
    #         if lst[i][k]:
    #             lst[i][k] = 0       # 한번 검사하면 0으로해서 다시 검사하지 않게
    #             cnt += 1
    #         else:
    #             if cnt == K:
    #                 result += 1
    #             cnt = 0
    # return result
    result = 0              # 중간에 while문을 쓰면 값을 바꾸지 않고 중복된 수를 체크하지 않아도 된다
    for i in range(N+1):
        j = 0
        cnt = 0
        while j<N+1:
            if lst[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
            j += 1
    return result

T = int(input())
for tc in range(1,T+1):
    result = 0
    N, K = map(int, input().split())
    lst = [list(map(int, input().split()))+[0] for _ in range(N)]
    lst.append([0]*(N+1))           # 체크하기 위해 제일 오른쪽과 아래에 0으로된 행열을 추가
    # lst_ruin = copy.deepcopy(lst)   # check 과정에서 값이 바뀌므로 하나 더 생성
    # arr = list(map(list, zip(*arr)))
    a = check(lst, N, K)
    for i in range(N):
        for j in range(N):
            if i>j:
                lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    a += check(lst, N, K)
    print(f'#{tc} {a}')