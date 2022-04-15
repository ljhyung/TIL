N, K = map(int, input().split())
lst = [int(input()) for _ in range(N)]
lst = lst[::-1]
cnt = 0
for i in range(N):
    if K>=lst[i]:
        cnt += K//lst[i]
        K %= lst[i]

print(cnt)