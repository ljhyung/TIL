n, m = map(int, input().split())
sqr = []
final = 1
le = min(n,m)
for _ in range(n):
    sqr.append(input())
#
for j in range(n):                      # 검사 기준 리스트라인 선택
    for i in range(min(n,m),0,-1):    # 검사할 사각형 길이를 i에 할당
        if ((j+i-1)<n):
            for k in range(m-i+1):                  # 라인 중 검사할 k번째 숫자 선택
                if ((k+i-1)<m) and (sqr[j][k] == sqr[j][k+i-1] == sqr[j+i-1][k] == sqr[j+i-1][k+i-1]):
                    if i > final:
                        final = i

# for j in range(n):
#     for i in range(m):
#         for k in range(le):
#             if (((j+k)<n) and ((k+i)<m) and (sqr[j][i] == sqr[j][i+k] == sqr[j+k][i] == sqr[j+k][i+k])):
#                 if k >= final:
#                     final = k+1

print(final**2)