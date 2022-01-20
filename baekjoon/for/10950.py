T = int(input())
A = []
B = []
for i in range(T):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(T):
    print(A[i] + B[i])