# _*_ coding: utf-8 _*_
#6317.py

def max(*num):
    k = num[0]
    for i in range(1,len(num)):
        if num[i] > k:
            k = num[i]
    return k


print("max(3, 5, 4, 1, 8, 10, 2) => {0}".format(max(3, 5, 4, 1, 8, 10, 2)))

