from math import ceil

N, kim, im = list(map(int, input().split()))
cnt = 0
while kim != im:
    kim -= kim//2
    im -= im//2
    cnt += 1
print(cnt)

# def check(Kim, Im):
#     kims = 0
#     ims = 0
#     for i in range(1, 18):
#         if Kim <= 2 ** i:
#             kims = i
#             break
#     for i in range(1, 18):
#         if Im <= 2 ** i:
#             ims = i
#             break
#     if kims != ims:
#         return (max(kims, ims))
#     else:
#         Kim = Kim - 2 ** (kims - 1)
#         Im = Im - 2 ** (ims - 1)
#         return check(Kim, Im)
#
# if N%2 and (N == im or N == kim):
#     print(N//2)
# else:
#     print(check(kim, im))


