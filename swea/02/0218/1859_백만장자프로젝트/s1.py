import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    maxnum = lst[-1]
    profit = 0
    for i in range(N-2, -1, -1):
        if maxnum < lst[i]:
            maxnum = lst[i]
        else:
            profit += maxnum-lst[i]
    print(f'#{tc} {profit}')






# arr = [[1,2,3], [4,5,6], [7,8,9]]
# arr = list(map(list, zip(*arr)))
# test = (1,4,7)
# print(list(test))
# print(arr)