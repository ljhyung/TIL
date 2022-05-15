
lst = [[1,0],[0,1]]
for j in range(2,41):
    lst += [[lst[j-1][0]+lst[j-2][0],lst[j-1][1]+lst[j-2][1]]]
T = int(input())
for i in range(T):
    N = int(input())
    print(*lst[N])
