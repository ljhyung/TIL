# '''
# https://www.acmicpc.net/problem/1786
# 찾기
# 플래티넘 5
#
# '''
# T = list(input())
# P = input()
#
# lst = [0 for _ in range(len(P))]
# cnt=0
# for i in range(1,len(P)):
#     if P[cnt]==P[i]:
#         lst[i]=cnt
#         cnt+=1
#     elif P[cnt]!=P[i]:
#         lst[i]=cnt
#         cnt=0
#         if P[i]==P[cnt]:
#             cnt+=1
#
# cnt=0
# answer = []
# head = 0
# idx = 0
# while head<=len(T)-len(P):
#     temp = head
#     while idx<=len(P):
#         if idx==len(P):
#             cnt+=1
#             answer.append(temp+1)
#             head = temp+idx if idx else temp+1
#             idx = lst[idx]
#             break
#         if T[temp+idx]==P[idx]:
#             idx+=1
#             continue
#         else:
#             head = temp+idx if idx else temp+1
#             idx = lst[idx]
#             break
#
#
# # print(lst)
# print(cnt)
# print(*answer)

import sys

T = sys.stdin.readline().replace("\n", "")  # 문자열
P = sys.stdin.readline().replace("\n", "")  # 패턴

KMPTable = [0 for _ in range(len(P))]


def MakeTable(P, KMPTable):
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:  # 같지않을때
            j = KMPTable[j - 1]  # 이전의 맞은부분곳까지 돌아가서 다시비교
        if P[i] == P[j]:  # 같을시
            j += 1  # j를 증가시키고
            KMPTable[i] = j  # 테이블 갱신


def KMP(T, P, KMPTable):
    MakeTable(P, KMPTable)
    j = 0
    count = 0
    result = []
    P_size = len(P)
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:  # 같지않을때
            j = KMPTable[j - 1]  # 이전의 맞은부분곳까지 돌아가서 다시비교
        if T[i] == P[j]:  # 같으면
            if j == P_size - 1:
                count += 1  # 개수 추가
                result.append(i - P_size + 2)  # 위치추가
                j = KMPTable[j]  # 위치를 옮겨주고 다시탐색
            else:  # j를 늘려준다
                j += 1
    return count, result

count, result = KMP(T,P,KMPTable)
print(count)
print(*result)