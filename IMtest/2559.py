# 투포인터
N, K = map(int, input().split())
lst = list(map(int, input().split()))
total = sum(lst[0:K])
max_total = total
for i in range(1,N-K+1):
    total = total - lst[i-1] + lst[i+K-1]
    if max_total<total:
        max_total = total
print(max_total)