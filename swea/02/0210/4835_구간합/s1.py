import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())


# def bubble_sort(lst, N):
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]


for i in range(tc):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    check = []
    for j in range(N-M+1):
        check.append(sum(lst[j:j+M]))       # 구간을 슬라이싱해 합을 구한다


    # bubble_sort(check, N-M+1)               # 구간합들을 정렬
    print(f'#{i+1} {abs(check[0] - check[-1])}')

# swea 사이트 제출 시 런타임에러가 난다