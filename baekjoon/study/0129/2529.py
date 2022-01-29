N = int(input())
up_down = input().split()
check = [False] * N
# 깊이, 값을 채웠는지, 이미 썼는지, 정답 리스트, 재귀
# result = []
depth = 1

def check_put(n1, n2, up_down):
    if up_down == '<':
        return n1 < n2
    else:
        return n1 > n2


def backtracking(result):
    global depth
    global up_down
    if depth == N+2:
        print(''.join(map(str, result)))
        return

    for i in range(N):
        if not check[i]:
            if depth == 1:
                result.append(i)
                check[0] = True
                depth += 1
                backtracking(result)
            if check_put(result[-1],i,up_down[depth-2]):
                result.append(i)
                check[depth-1] = True
                depth += 1
                backtracking(result)

backtracking([])



        # for i in range(N):
        #     if i not in result:
        #         if put_num(i, up_down[j]):
        #             break