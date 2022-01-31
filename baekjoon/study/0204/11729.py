def hanoi(N):
    if N == 1:
        return 1
    return hanoi(N-1)*2 +1

def path(N, x, y, z):
    if N ==1:
        return (x, z)
    return path(N-1, x, z, y) + (x, z) + path(N-1, y, x, z)

N = int(input())

print(hanoi(N))

result = path(N, 1, 2, 3)
for i in range(len(result)//2):
    print(str(result[2*i]) + ' ' + str(result[2*i+1]))