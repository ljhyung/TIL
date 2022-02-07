N = int(input())
cnt = 0
if N == 1:
    cnt = 1
else:
    while N>1:
        N = N - 6*cnt
        cnt+=1
print(cnt)