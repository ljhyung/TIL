K = int(input())
lst = []
# E = {}
# W = {}
# S = {}
# N = {}
hor_max = [0, 0]
ver_max = [0, 0]
for i in range(6):
    lst.append(list(map(int, input().split())))
    if lst[i][0] == 1 or lst[i][0] == 2:
        if lst[i][1] > ver_max[1]:
            ver_max[0] = i
            ver_max[1] = lst[i][1]
    if lst[i][0] == 3 or lst[i][0] == 4:
        if lst[i][1] > hor_max[1]:
            hor_max[0] = i
            hor_max[1] = lst[i][1]
a = hor_max[1]*ver_max[1]
b = abs(lst[hor_max[0]-1][1] - lst[(hor_max[0]+1)%6][1])
c = abs(lst[ver_max[0]-1][1] - lst[(ver_max[0]+1)%6][1])
print(K*(a-(b*c)))

#     if lst[i][0] == 1:
#         E[i] = lst[i][1]
#     if lst[i][0] == 2:
#         W[i] = lst[i][1]
#     if lst[i][0] == 3:
#         S[i] = lst[i][1]
#     if lst[i][0] == 4:
#         N[i] = lst[i][1]
# print(sum(E.values()) * sum(N.values()))
