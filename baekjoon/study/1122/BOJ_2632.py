'''
https://www.acmicpc.net/problem/2632
피자판매
골드2
3시간
'''
import sys
input = sys.stdin.readline
N = int(input())
A,B = map(int, input().split())
cnt=0
sumAlst = [0]*2000001
sumAlst[0]=1
sumBlst = [0]*2000001
sumBlst[0]=1
pA = []
pB = []
for _ in range(A):
    pA.append(int(input()))
for _ in range(B):
    pB.append(int(input()))
pA += pA
pB += pB
headA=0
tailA=headA+1
headB=0
tailB=headB+1

while True:
    tempSA = sum(pA[headA:tailA])
    if tempSA>N:
        headA+=1
        tailA=headA+1
        if headA==A:break
        continue
    else:
        sumAlst[tempSA]+=1
    tailA += 1
    if tailA%A==headA:
        headA+=1
        tailA=headA+1
        if headA==A:break
        continue

sumAlst[sum(pA[:A])]+=1
while True:
    tempSB = sum(pB[headB:tailB])
    if tempSB>N:
        headB +=1
        tailB =headB+1
        if headB==B:
            break
        continue
    else:
        sumBlst[tempSB]+=1
    tailB+=1
    if tailB%B==headB:
        headB +=1
        tailB =headB+1
        if headB==B:
            break
        continue
if B!=1:
    sumBlst[sum(pB[:B])]+=1

for i in range(N+1):
    cnt += sumAlst[i]*sumBlst[N-i]

print(cnt)
