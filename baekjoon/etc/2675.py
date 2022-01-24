N = int(input())
lst = []

for i in range(N):
    cnt = 0
    final = ''
    lst.append(list(input().split()))
    cnt = lst[i][0]
    for k in range(len(lst[i][1])):
        final += lst[i][1][k] * int(lst[i][0])
    print(final)



