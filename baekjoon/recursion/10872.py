def fac(N):
    if N <= 1:
        return 1
    return N * fac(N-1)

num = int(input())

print(fac(num))