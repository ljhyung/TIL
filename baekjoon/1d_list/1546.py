import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
avg = 0

for score in scores:
    avg += score * 100 / (N * max(scores))

print(avg)