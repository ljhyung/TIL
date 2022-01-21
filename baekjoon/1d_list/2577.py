# numbers = list(int(input()) for _ in range(3))
# result = [0] * 10
#
# mul = numbers[0] * numbers[1] * numbers[2]
# mul_str = str(mul)
#
# for i in mul_str:
#     result[int(i)] = int(result[int(i)])+1
#
# for i in result:
#     print(i)

mul = 1
for _ in range(3):
    n = int(input())
    mul *= n

mul = list(map(int, str(mul)))
for i in range(10):
    print(mul.count(i))
