from math import sqrt



def sosu(num):
    sosu_list = [True] * (2*num + 1)        # 소수를 체크하기 위한 리스트
    sosu_list[0] = False                    # 0과 1은 false로 설정
    sosu_list[1] = False
    for i in range(2, int(sqrt(2*num))+1):  # 숫자의 제곱근까지만 검사
        if sosu_list[i]:                    # 이미 다른 수의 배수인지 검사
            j = 2
            while i*j <= 2*num:
                sosu_list[i*j] = False
                j += 1
    cnt = 0
    for k in range(num+1,2*num+1):          # 검사하는 숫자 초과 2배 이하를 체크
        if sosu_list[k]:
            cnt += 1
    return cnt

while True:
    cnt = 0
    n = int(input())
    if not n:                               # 0이면 결과 안 나게
        break
    print(sosu(n))

# 주어진 문제 범위만큼 소수 미리 구하는 방법
# def sosu(num):
#     if num == 1:
#         return False
#
#     for i in range(2, int(sqrt(num))+1):
#         if num % i == 0:
#             return False
#
#     return True
#
# lst = list(range(2,246912))
# sosulst = []
# for i in lst:
#     if sosu(i):
#         sosulst.append(i)
#
#
# while True:
#     cnt = 0
#     n = int(input())
#     if not n:
#         break
#
#     for i in sosulst:
#         if n < i <= n*2:
#             cnt += 1
#
#     print(cnt)


# 시간 초과 난 방법
# while True:
#     n = int(input())
#     if not n:
#         break
#     cnt = 0
#     for i in range(n+1, 2*n + 1):
#         for k in range(2, int(sqrt(i)) + 1):
#             if i % k == 0:
#                 break
#         else:
#             cnt += 1
#     print(cnt)
