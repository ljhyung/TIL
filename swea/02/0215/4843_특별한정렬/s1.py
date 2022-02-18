import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

def my_max_idx(lst):                    # 제일 큰 값의 인덱스를 반환
    result = 0
    for i in range(len(lst)):
        if lst[result] < lst[i]:
            result = i
    return result


def my_min_idx(lst):                    # 제일 작은 값의 인덱스를 반환
    result = 0
    for i in range(len(lst)):
        if lst[result] > lst[i]:
            result = i
    return result


for i in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    for j in range(10):                             # 10개까지만 출력이니깐 10까지
        if j%2:                                     # 짝수 인덱스일 때는 최소
            cid = my_min_idx(lst[j:])               # 정렬 안 된 현재 검사 인텍스부터 끝까지를 범위로
           lst[j], lst[cid+j] = lst[cid+j], lst[j]  # 제일 큰 값과 검사 값을 교환
        else:                                       # 홀수 인덱스일 때는 최대
            cid = my_max_idx(lst[j:])
            lst[j], lst[cid+j] = lst[cid+j], lst[j] #
    a = ' '.join(map(str, lst[:10]))                # 10개까지만 제출
    print(f'#{i+1} {a}')