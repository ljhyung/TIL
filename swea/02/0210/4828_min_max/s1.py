import sys
sys.stdin = open('input.txt', 'r')

tc = int(input())

def bubble_sort(lst, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


for i in range(tc):
    N = int(input())
    lst = list(map(int, input().split()))
    bubble_sort(lst, N)
    print(f'#{i+1} {lst[-1]-lst[0]}')