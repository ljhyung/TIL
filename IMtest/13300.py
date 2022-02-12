from math import ceil

lst = [[0,0] for i in range(6)]
N, oneroom = map(int, input().split())
for i in range(N):
    gender, grade = map(int, input().split())
    lst[grade-1][gender] += 1
cnt = 0
for i in range(6):
    for j in range(2):
        cnt += ceil(lst[i][j]/oneroom)
print(cnt)





# man = [0 for i in range(7)]
# woman = [0 for i in range(7)]
#
# N, oneroom = map(int, input().split())
# for i in range(N):
#     gender, grade = map(int, input().split())
#     if gender:
#         man[grade] += 1
#     else:
#         woman[grade] += 1
# cnt = 0
# for i in man:
#     cnt += ceil(i / oneroom)
# for i in woman:
#     cnt += ceil(i / oneroom)
#
# print(cnt)