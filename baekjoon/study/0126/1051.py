n, m = map(int, input().split())
sqr = []
final = 1
le = min(n,m)
for _ in range(n):
    sqr.append(input())
#
for j in range(n):                      # 검사 기준 리스트라인 선택
    for i in range(min(n,m),0,-1):    # 검사할 사각형 길이를 i에 할당
        if ((j+i-1)<n):                 # 검사하는 수에서 사각형 길이 i만큼 오른쪽으로 이동했을 때 인덱스 벗어나는지 판단
            for k in range(m-i+1):                  # 라인 중 검사할 k번째 숫자 선택
                if ((k+i-1)<m) and (sqr[j][k] == sqr[j][k+i-1] == sqr[j+i-1][k] == sqr[j+i-1][k+i-1]):
                    # 검사하는 수에서 사각형 길이 i만큼 밑으로 이동했을 때 인덱스 벗어나는지 판단
                    # 네 꼭지점 수가 같은지 검사
                    if i > final:   # 제일 큰 사각형 판별
                        final = i

# for j in range(n):
#     for i in range(m):
#         for k in range(le):
#             if (((j+k)<n) and ((k+i)<m) and (sqr[j][i] == sqr[j][i+k] == sqr[j+k][i] == sqr[j+k][i+k])):
#                 if k >= final:
#                     final = k+1

print(final**2)