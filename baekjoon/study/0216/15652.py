N, depth = map(int, input().split())
num = [i for i in range(1, N + 1)]
result = []


def suyeol(N, depth):
    if not depth:
        print(*result)
        return
    for i in range(N):
        if not len(result) or num[i] >= result[-1]:
            result.append(num[i])
            suyeol(N, depth-1)
            result.pop()

suyeol(N,depth)

# def suyeol(N, depth, start):
#     if not depth:
#         print(*result)
#         return
#     for i in range(start,N):
#         result.append(num[i])
#         suyeol(N, depth-1, i)
#         result.pop()
#
# suyeol(N,depth,0)
