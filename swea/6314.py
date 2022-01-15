# _*_ coding: utf-8 _*_
#6314


num = []
for i in range(1,11):
    num.append(i)

k = filter(lambda n: n%2 == 0, num)

print(list(k))