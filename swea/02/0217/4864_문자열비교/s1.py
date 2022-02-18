import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(T):         # in으로 간단하게 할 수 있다
    P = input()
    word = input()
    result = 0
    for i in range(len(word)-len(P)+1):       # 비교길이만큼 뒤는 빼주기
        for j in range(len(P)):
            if P[j] != word[i+j]:
                break
        else:                           # break 없이 통과하면 있다고 체크
            result = 1
            break
    print(f'#{tc+1} {result}')






for i in range(5):
    if i>3:             # i>6
        break
    print(i)
else:
    print('end')
