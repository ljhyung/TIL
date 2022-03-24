import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, nums = input().split()
    dnum = ''
    for num in nums:
        dnum += f'{int(num, base=16):04b}'
    print(f'#{tc} {dnum}')