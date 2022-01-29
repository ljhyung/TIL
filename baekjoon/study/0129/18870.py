import sys

N = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst2 = list(sorted(set(lst)))
dic = {lst2[i]:i for i in range (len(lst2))}
for i in lst:
    print(dic[i], end=' ')


# for i in lst:
#     for j in range(N):
#         if i == lst2[j]:
#             print(j, end=' ')
#             break


# flst = lst.copy()
# for i in range(N):
#     flst[i] = sorted(lst).index(lst[i])
# print(flst)


# for i in range(N):
#     test_set = set()
#     for j in range(N):
#         if lst[i] > lst[j]:
#             test_set.add(lst[j])
#     nlst.append(len(test_set))
#
# print(' '.join(map(str, nlst)))