N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[0]))
cnt = 0
e = 0
for i in lst:
    if i[0]>=e:
        cnt += 1
        e = i[1]
print(cnt)