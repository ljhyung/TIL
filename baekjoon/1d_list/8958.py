# N = int(input())
# test_list = []
# cnt = 0
# score = []
#
# for p in range(N):
#     test_list.append(input())
#
# for j in range(N):
#     score.append(0)
#     for i in range(len(test_list[j])):
#         if test_list[j][i] == 'O':
#             cnt += 1
#             score[j] += cnt
#         else:
#             cnt = 0
#     cnt = 0
#
# for k in range(N):
#     print(score[k])

n = int(input())

for i in range(n):
    Os =input().split("X")
    Os = [len(k) for k in Os]
    points =0
    for boy in Os:
        points += int((boy+1)*boy/2)
    print(points)