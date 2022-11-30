'''
https://www.acmicpc.net/problem/1052
물병
실버1

'''
import math
n,k = map(int,input().split())
cnt=0
lst = []
while n:
    lst.append(n%2)
    n//=2
lst.append(0)

L = len(lst)
def sol():
    global cnt
    while sum(lst)>k:
        for i in range(L):
            if lst[i]:
                temp=i
                cnt += 2 ** temp
                while True:
                    lst[temp]=0
                    lst[temp+1]+=1
                    if lst[temp+1]<2:
                        break
                    else:
                        temp+=1

                break


sol()

print(cnt)