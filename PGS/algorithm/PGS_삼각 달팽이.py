def solution(n):
    answer = []
    lst = [[0]*n for _ in range(n)]
    N = n
    minus = 0
    rr, cc = -1, 0
    count = 1
    while (N-minus)!=0:
        for i in range(N-minus):
            if minus%3==0:
                rr += 1
            elif minus%3==1:
                cc += 1
            else:
                rr -= 1
                cc -= 1
            lst[rr][cc] = count
            count += 1
        minus += 1
    for r in range(n):
        for c in range(n):
            if lst[r][c]:
                answer.append(lst[r][c])

    print(lst)
    return answer

solution(3)