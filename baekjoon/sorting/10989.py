import sys

lst = [0]*10001
n = int(input())
for i in range(n):
    lst[int(sys.stdin.readline())] += 1
for i in range(10001):
    while lst[i]:
        print(i)
        lst[i] -= 1