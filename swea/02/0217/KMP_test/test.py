# input.txt
# 5
# AAACAAAAB
# ABCAABCBA
# ACACAACACC
# ABCAABCACABACA
# ACACABACACACAB
#
# output.txt
# #1 -1 0 1 2 0 1 2 3 3
# #2 -1 0 0 0 1 1 2 3 0
# #3 -1 0 0 1 2 3 1 2 3 4
# #4 -1 0 0 0 1 1 2 3 4 0 1 2 1 0
# #5 -1 0 0 1 2 3 0 1 2 3 4 5 4 5


# def LPS_table(word):
#     s = 0
#     table = [-1] + [0]*len(word)
#     for i in range(1,len(word)):
#         table[i] = s
#         if word[i] == word[s]:
#             s += 1
#         else:
#             while s > 0 and word[i] != word[s]:
#                  s = table[s]
#                  table[i] = s
#     print(table)

def make_lps(P):
    len_p = len(P)
    lps = [0] * len_p

    lps[0] = -1  # 의미
    s = 0   # 몇 번째까지 패턴인지

    for p_idx in range(1, len_p):
        lps[p_idx] = s  # 현재 패턴의 위치에 이전의 s 값 대입
        # if P[p_idx] == P[s]:
        #     s += 1
        # else:
        while s > 0 and P[p_idx] != P[s]: # 이전 패턴들과 같지 않으면 계속 비교
            s = lps[s]                    # 디버거로 꼭 살펴보긔!!!!

        if P[p_idx] == P[s]:
            s += 1

    return lps

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    P = input()

    lps = make_lps(P)
    print(f'#{tc} {lps}')
