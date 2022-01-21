## set 이용해서 중복 없애보자
numbers = []
result = []
for i in range(10):
    numbers.append(int(input()))

for num in numbers:
    result.append(num%42)

cnt = 0
for _ in set(result):
    cnt += 1

print(cnt)