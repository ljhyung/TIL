N = int(input())
lst = map(int, input().split())

cnt = 0
for i in lst:
    if i == 1:
        cnt += 1
    for k in range(2,i):
        if i%k == 0:
            cnt += 1
            break


print(N-cnt)