# _*_ coding: utf-8 _*_
#6315.py

num = []
for i in range(1,11):
    num.append(i)

k = map(lambda n: n**2, num)

print(list(k))