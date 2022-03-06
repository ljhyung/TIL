N = int(input())
lst = list(map(int, input().split()))
check = []
for i in range(N):
    if lst[i] == 0 :
        check.append(i+1)
    else:
        check.insert(i-lst[i], i+1)
print(' '.join(map(str, check)))