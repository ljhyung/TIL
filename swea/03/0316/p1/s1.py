import sys
sys.stdin = open("input.txt", "r")


def pre_order(T):
    if T:
        print(T,end=' ')
        pre_order(lst[T][0])
        pre_order(lst[T][1])

def in_order(T):
    if T:
        pre_order(lst[T][0])
        print(T, end=' ')
        pre_order(lst[T][1])

def post_order(T):
    if T:
        pre_order(lst[T][0])
        pre_order(lst[T][1])
        print(T, end=' ')

V = int(input())
lst = [[0, 0, 0] for _ in range(V+1)]
temp = list(map(int, input().split()))
for i in range(0,len(temp),2):
    p, c = temp[i], temp[i+1]
    if lst[p][0]==0:
        lst[p][0] = c
    else:
        lst[p][1] = c
    lst[c][2] = p

root = 0
for i in range(1, V+1):
    if lst[i][2] ==0:
        root = i
        break


pre_order(root)
print()
in_order(root)
print()
post_order(root)
