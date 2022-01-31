M, N = map(int, input().split())
check = False
for i in range(M, N+1):
    if i > 1:
        for k in range(2, int(i**0.5)+1):
            if i%k == 0:
                check = True
                break
        if not check:
            print(i)
        check = False

# M, N = map(int, input().split())
#
# for i in range(M, N + 1):
#     if i == 1:
#         continue
#
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#
#     else:                     # for else문 주의
#         print(i)