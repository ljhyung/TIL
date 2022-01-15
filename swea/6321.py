# _*_ coding: utf-8 _*_
#6321

def sosu(num):
    k=0
    for i in range(1,num):
        if num%i == 0:
            k += 1

    if k == 1:
        return True
    else:
        return False

a = int(input())
if sosu(a):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")