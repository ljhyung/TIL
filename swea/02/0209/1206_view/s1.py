import sys
sys.stdin = open('input.txt', 'r')


def bubble_sort(a, N): # 수업시간에 배운 버블정렬 이용해봤습니다
    for i in range(N-1, 0, -1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]


for tc in range(10):
    N = int(input())
    lst = list(map(int, input().split()))
    total = 0
    for i in range(2, len(lst)-2):  # 젤 오른쪽과 왼쪽 건물은 00 이므로 인덱스 에러 날까봐 그냥 첨부터 range를 이렇게 잡았습니다
        test_list = lst[i-2:i+3]    # 중심 건물 포함 주위 5건물을 슬라이싱해서 새로운 리스트로 할당
        bubble_sort(test_list, 5)   # 버블정렬
        if lst[i] == test_list[-1] and lst[i] != test_list[-2]: # 선택한 건물이 제일 큰 건물이고 같은 높이의 건물이 있지 않은지 체크했습니다
            total += lst[i] - test_list[-2] # 제일 높은 건물의 층수에서 두 번째로 높은 건물 층수를 빼면 조망권 확보된 층수가 나옵니다
    print(f'#{tc+1} {total}')
