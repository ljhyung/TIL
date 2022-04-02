import sys
sys.stdin = open("input.txt", "r")

lst = input().strip('[]').split(', ')
for i in range(len(lst)):
    lst[i] = lst[i].strip('"')

print(lst, type(lst))