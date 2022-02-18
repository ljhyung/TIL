import sys
sys.stdin = open('input.txt', 'r')


def my_max(lst):        # 최고값 찾기
    max = lst[0]
    for i in lst:
        if max < i:
            max = i
    return max

T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    dict = {}
    for i in str1:
        dict[i] = 0             # 찾는 글자들 dictionary에 넣기
    # dict = {i:0 for i in str1}
    for j in str2:
        for k in dict.keys():
            if k == j:          # 글자를 찾으면 딕셔너리의 해당 키 값의 값 증가
                dict[k] += 1
    a = list(dict.values())
    print(f'#{tc+1} {my_max(a)}')