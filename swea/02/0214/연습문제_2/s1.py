import sys
sys.stdin = open("input.txt", "r")

tc = int(input())
for i in range(tc):
    lst  = list(map(int, input().split()))
    cnt = 0
    for j in range(1,1<<len(lst)):          # 1에서 시작해야, 부분집합의 갯수만큼 반복문
        total = 0
        for k in range(len(lst)):           # 리스트의 인덱스마다 체크
            if j&(1<<k):                    # 부분 집합에 값이 존재하면
                total += lst[k]             # 부분 집합의 합에 값을 더한다
        if not total:
            cnt = 1
    print(f'#{i+1} {cnt}')


# arr = [3,6,7]
# n = len(arr)
# for i in range(1<<n):
#     for j in range(n):
#         if i&(1<<j):
#             print(arr[j], end=', ')
#     print()