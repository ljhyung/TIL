# from math import sqrt
# # non_squars = [x for x in range(101) if sqrt(x)**2 != x]
# # print(non_squars)
# a = sqrt(5)**2 != 5
# print(a)
#
# import keyword
# print(keyword.kwlist)

# import math
# a = 3.5-3.12
# b = 0.38
# math.isclose(a,b)
#
# i = [i for i in range(1,50,2)]
# print(i)
# j = [i for i in range(1,50)][0:49:2]
# print(j)
#
# s = 'abcdefghi'
# s = s[::-1]
# print(s)
#
# 3.
# std = {'강보경':'26', '고광' : '27', '김다은' : '24'}
# print(std)
# print(type(std))

# 4.
# n = 5
# m = 9
#
# for _ in range(m):
#     for _ in range(n):
#         print('*', end = '')
#     print('')
#
# 5.
# temp = 36.5
# print('입실 불가') if temp >= 37.5 else print('입실 가능')
# 6.
# scores = [80, 89, 99, 83]
# t = 0
# total = 0
# for i in scores:
#     t += 1
#     total += i
# print(total/t)
#
# 1.
# N = int(input())
#
# for i in range(1,N+1):
#     if N % i == 0:
#         print(i, end = ' ')
#
# 2.
# numbers = [
#     85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
#     51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
#     52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
# ]
# sorted_numbers = sorted(numbers)
#
# t = 0
# for i in sorted_numbers:
#     t += 1
# if t%2 == 0:
#     print(sorted_numbers[int(t / 2)], sorted_numbers[int(t / 2)+1])
# else:
#     print(sorted_numbers[int(t / 2) + 1])
# 3.
# number = int(input())
# str = ''
# for i in range(1,number+1):
#     for j in range(1,i+1):
#         if j == i:
#             print(f'{j}')
#         else:
#             print(f'{j}', end= ' ')

# r = 10
# area = r * r**2
# print(type(area))
# result = 'Area: ' + str(area)
# is_small = area<100
# print(is_small)
#
# def cube(num):
#     return num**3
#
# print(cube(2))
# print(cube(100))

# def rec(height, width):
#
#     return height * width, 2* (height + width)
#
# print(rec(30, 20))
#
# scores = [80, 89, 99, 83]
# t = 0
# total = 0
# for i in scores:
#     t += 1
#     total += i
# print(total/t)






