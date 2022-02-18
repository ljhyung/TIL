import sys

sys.stdin = open('input.txt', 'r')

# 홀 짝판별
N = int(input())
if N % 1:
    print(1)
else:
    print(0)

# 입력 받은 수 합 구하기
num = list(map(int, input().split()))
total = 0
for i in num:
    total += i
print(total)

# 이중 리스트 만들기
N = int(input())
lst = []
for i in range(N):
    lst.append(list(map(int,input().split())))

print(lst)