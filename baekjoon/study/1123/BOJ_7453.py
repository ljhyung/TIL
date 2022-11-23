'''
https://www.acmicpc.net/problem/7453
합이 0인 네 정수
골드2
1430
'''
import sys
input = sys.stdin.readline
n = int(input())
A = []
B = []
C = []
D = []
cnt=0
for _ in range(n):
    a,b,c,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
A.sort()
B.sort()
C.sort()
D.sort()
lst1 = []
lst2 = []
dict1 = dict()
dict2 = dict()
for i in range(n):
    for j in range(n):
        temp = A[i]+B[j]
        if dict1.get(temp)==None:
            dict1[temp]=1
        else:
            dict1[temp] += 1
for i in range(n):
    for j in range(n):
        temp = C[i]+D[j]
        if dict1.get(-temp)!=None:
            cnt+=dict1.get(-temp)

# lst1.sort()
# lst2.sort()
# len2 = len(lst2)
# def search(num,l,r,pivot):
#     while True:
#         if l>r:return False
#         if lst2[pivot]==num:
#             return True
#         elif lst2[pivot]<num:
#             l=pivot+1
#             pivot = (l+r)//2
#             if l==r:
#                 if lst2[l]==num:
#                     return True
#                 return False
#             # search(num,l,r,pivot)
#             continue
#         elif lst2[pivot]>num:
#             r=pivot-1
#             pivot = (l + r) // 2
#             if l == r:
#                 if lst2[l]==num:
#                     return True
#                 return False
#             # search(num,l,r,pivot)
#             continue

# for i in range(len(lst1)):
#     temp = -lst1[i]
#     l=0
#     r=len2-1
#     pivot = len2//2
#     if search(temp,l,r,pivot):
#         cnt +=1

print(cnt)
# print(lst1, lst2)
# print(A,B,C,D)



