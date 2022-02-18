import sys
sys.stdin = open('input.txt', 'r')

# N, M으로 행렬 읽기
N, M = map(int, input().split())
numbers = []
for i in  range(N):
    numbers.append(input().split())

print(numbers)

# 1. 행 우선으로 요소를 출력해보세요
print('1. 행 우선으로 요소를 출력해보세요')
for i in range(N):
    for j in range(M):
        print(numbers[i][j], end=' ')
    print()
print('---------------')

# 2. 열 우선으로 요소를 출력해보세요
print('2. 열 우선으로 요소를 출력해보세요')
for j in range(M):
    for i in range(N):
        print(numbers[i][j], end=' ')
    print()
print('---------------')

# 3. 역순으로 행의 요소들을 출력해보세요
print('3. 역순으로 행의 요소들을 출력해보세요')
for i in range(N):
    for j in range(M-1, -1, -1):
        print(numbers[i][j], end=' ')
    print()
print('---------------')

# 4. 역순으로 열의 요소들을 출력해보세요
print('4. 역순으로 열의 요소들을 출력해보세요')
for j in range(M):
    for i in range(N - 1, -1, -1):
        print(numbers[i][j], end=' ')
    print()
print('---------------')

# 5. 지그재그로 순회해보세요
print('5. 지그재그로 순회해보세요')
for i in range(N):
    if i%2:
        for j in range(M - 1, -1, -1):
            print(numbers[i][j], end=' ')
    else:
        for j in range(M):
            print(numbers[i][j], end=' ')
    print()