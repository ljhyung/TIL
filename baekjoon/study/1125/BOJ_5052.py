'''
https://www.acmicpc.net/problem/5052
전화번호 목록
골드4
1시간
'''

def sol(n):
    flag = False
    nums = []
    for _ in range(n):
        nums.append(input())
    nums.sort(key=lambda x:len(x))
    for num in nums:
        if flag:break
        for i in range(1,len(num)+1):
            if phone.get(num[:i])!=None:
                flag=True
                break
        phone[num]=1
    if flag:
        return True
    else:
        return False


t = int(input())
for _ in range(t):
    n = int(input())
    phone = dict()
    if sol(n):
        print("NO")
    else:
        print("YES")






# # 깔끔코드
# import sys
# input = sys.stdin.readline
#
# t = int(input())
#
# def solution(calls):
#     calls = sorted(calls)
#
#     for i in range(len(calls)-1):
#         if calls[i+1].startswith(calls[i]):
#             return False
#     return True
#
# for _ in range(t):
#     N = int(input())
#     calls = [input().rstrip() for _ in range(N)]
#     print("YES" if solution(calls) else "NO")