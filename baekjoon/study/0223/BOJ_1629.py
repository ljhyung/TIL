def power(A,B):
    if B == 1:
        return A
    if B%2:
        return power(A, B//2) * power(A, B//2) * A
    else:
        return power(A, B//2) * power(A, B//2)
A, B, C = map(int, input().split())
print(power(A,B)%C)
