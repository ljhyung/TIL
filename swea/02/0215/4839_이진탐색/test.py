import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    P_lst = [i for i in range(1, P+1)]
    start_idx = 0
    end_idx = P-1

    for Px in (Pa, Pb):
        cnt = 0
        if Px == Pa:
            while start_idx <= end_idx:
                middle = (start_idx + end_idx) // 2
                if P_lst[middle] == Pa:
                    cnt += 1
                    break
                elif P_lst[middle] > Pa:
                    end_idx = middle
                    cnt += 1
                else:
                    start_idx = middle
                    cnt += 1
        result_A = cnt

        if Px == Pb:
            while start_idx <= end_idx:
                middle = (start_idx + end_idx) // 2
                if P_lst[middle] == Pb:
                    cnt += 1
                    break
                elif P_lst[middle] > Pb:
                    end_idx = middle
                    cnt += 1
                else:
                    start_idx = middle
                    cnt += 1
        result_B = cnt

    if result_A > result_B:
        print(f'#{tc} B')
    elif result_A < result_B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')