import sys
sys.stdin = open('input.txt', 'r')

def findword(lst,M):
    for i in lst:                           # 한 줄씩 검사
        for j in range(len(lst)-M+1):
            a = i[j:j+M]
            if a == a[::-1]:                # 회문 검사
                return a

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]
    zip_lst = list(zip(*lst))
    print(zip_lst)
    a = findword(lst, M)
    b = findword(zip_lst, M)        # 전치행렬
    if a:
        print(f"#{tc+1} {''.join(findword(lst, M))}")
    elif b:
        print(f"#{tc+1} {''.join(map(str, findword(zip_lst, M)))}")