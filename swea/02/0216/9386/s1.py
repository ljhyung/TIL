import sys
sys.stdin = open("input.txt", "r")

tc = int(input())

for i in range(tc):
    N = int(input())
    lst = input().split('0')
    max = 0
    for j in range(len(lst)):
        if len(lst[j]) > max:
            max = len(lst[j])
    print(f'#{i+1} {max}')