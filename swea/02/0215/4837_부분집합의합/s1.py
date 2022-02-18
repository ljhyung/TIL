import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

for i in range(tc):
    N, K = map(int, input().split())
    cnt = 0
    for j in range(1,1<<12):
        result = []

        # k=0             # 1번째 방법
        # while k<12 and len(result)<=N:  # 0.23886 sec ~ 0.24507 sec?
        #     if j&(1<<k):
        #         result.append(k+1)
        #     k += 1

        for k in range(12):       # 2번째 방법 0.24047 sec ~0.25313 sec?
            if j&(1<<k):
                result.append(k+1)

        if len(result)==N and sum(result)==K:   # 조건 만족하는지 검사
            cnt += 1
    print(f'#{i+1} {cnt}')

import math
import time
start = time.time()
math.factorial(100000)
end = time.time()
print(f"{end - start:.5f} sec")