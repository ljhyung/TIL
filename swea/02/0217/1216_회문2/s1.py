# 한 줄 검사위치부터 끝까지부터 같은 문자 있으면, 사이 길이가 회문길이보다 길면 회문 검사
# 회문 길이 저장하고 진행


import sys
sys.stdin = open('input1.txt', 'r')

result = 0
def findword(lst):
    global result                           # 글로벌 변수에 결과 넣어서 다른 검사할 때도 빨리 넘기기
    for i in lst:                           # 한 줄씩 검사
        for j in range(len(lst)):
            for k in range(len(lst)-1, j-1, -1):
                if i[j] == i[k] and k-j+1>result:            # 조건문 추가하면 시간 감소
                    a = i[j:k+1]
                    if a == a[::-1]:                # 회문 검사
                        result = len(a)
                        break
    return result

for tc in range(10):
    result = 0
    N = int(input())
    lst = [list(input()) for _ in range(100)]
    zip_lst = list(zip(*lst))
    findword(lst)
    findword(zip_lst)
    print(f'#{tc+1} {result}')
