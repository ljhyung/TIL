import sys
sys.stdin = open("input.txt", "r")

def my_max(lst):
    result = 0
    for i in lst:
        if result <= i:
            result = i
    return result

for tc in range(10):
    N = int(input())
    sum_lst = [0 for _ in range(202)]           # 0~99까지는 행의 합, 100~199까지는 열의 합, 200,201은 대각선 합
    lst = [list(map(int, input().split())) for _ in range(100)]
    flip_lst = list(zip(*lst))                  # zip으로 전치 행렬을 만들어 합 구하기 편하게
    for j in range(100):
        sum_lst[j] = sum(lst[j])
        sum_lst[j+100] = sum(flip_lst[j])
        sum_lst[200] += lst[j][j]               # 대각선 왼쪽 위에서 오른쪽 아래로
        sum_lst[201] += lst[j][99-j]            # 오른쪽 위에서 왼쪽 아래로
    print(f'#{tc+1} {my_max(sum_lst)}')