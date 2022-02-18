# aaaaaa, aaa 엣지케이스
# aaapaa aap

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T):
    A, B = input().split()
    cnt = 0
    i = 0
    while i < len(A) - len(B)+1:        # <=이랑 고민했는데 <=를 추가하거나 +1을 추가하거나 둘 중 하나를 하면 됐는데 둘 다
        for k in range(len(B)):         # 절묘하게 피해서 답이 안 나왔다 생각을 좀 더 하고 작성해야하는데...
            if B[k] != A[i+k]:
                i += 1
                break
        else:                           # break 없이 for문 끝나면 단어 일치
            cnt += 1
            i = i + len(B)              # 일치하는 단어가 있으면 그 단어가 끝난 다음 인덱스부터 탐색
    result = len(A) - cnt*(len(B)-1)
    print(f'#{tc+1} {result}')
