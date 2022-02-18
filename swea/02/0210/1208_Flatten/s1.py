import sys
sys.stdin = open('input.txt', 'r')

def my_max(lst):                    # 최댓값의 인덱스 구하기
    max_id = 0
    for ii in range(len(lst)):
        if lst[ii] > lst[max_id]:
            max_id = ii
    return max_id


def my_min(lst):                    # 최솟값의 인덱스 구하기
    min_id = lst[0]
    for ii in range(len(lst)):
        if lst[ii] < lst[min_id]:
            min_id = ii
    return min_id


for i in range(10):
    Dump = int(input())
    lst = list(map(int, input().split()))
for dumping in range(Dump):         # 각 덤프마다 최대-1, 최소+1
        lst[my_max(lst)] -= 1
        lst[my_min(lst)] += 1
    print(f'#{i+1} {lst[my_max(lst)] - lst[my_min(lst)]}')  # 차이를 출력
