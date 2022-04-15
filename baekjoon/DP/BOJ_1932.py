n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(lst[i])):
        if 1<=j<len(lst[i])-1:
            lst[i][j] = lst[i][j] + max(lst[i-1][j-1], lst[i-1][j])
        elif j==0:
            lst[i][j] = lst[i][j] + lst[i-1][j]
        elif j==len(lst[i])-1:
            lst[i][j] = lst[i][j] + lst[i-1][j-1]

print(lst)
print(max(lst[n-1]))