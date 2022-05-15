def fac(k):
    res = 1
    for i in range(1,k+1):
        res *= i
    return res

n, m = map(int, input().split())
answer = fac(n)//(fac(m)*fac(n-m))

print(answer)