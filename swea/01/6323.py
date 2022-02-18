# _*_ coding: utf-8 _*_
#6323.py

def pibo(num):
    pibona = [1,1]
    for i in range(2,num):
        k = pibona[i-1] + pibona[i-2]
        pibona.append(k)
    return pibona

number = int(input())
print(pibo(number))
