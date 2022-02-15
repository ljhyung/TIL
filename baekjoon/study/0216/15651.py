# import copy                           # 시간 초과 떠서 칼질

N, depth = map(int, input().split())
# check = [False for _ in range(N)]     # 같은 수 체크 안 함
num = [i for i in range(1, N + 1)]
result = []
# real_result = []
def suyeol(N, depth):
    if not depth:
        # a = copy.deepcopy(result)
        # return real_result.append(a)  # 결과 저장 안 하고 바로 출력
        print(*result)
        return
    for i in range(N):
        # if not check[i]:
        #     check[i] = True
        result.append(num[i])
        # depth -= 1
        suyeol(N, depth-1)              # 깊이 빼고 더하지 말고 그냥 여기서 조작
        result.pop()
        # depth += 1
            # check[i] = False
#     return real_result                # return값 필요 없음
#
# b = suyeol(N,depth)
# for i in range(len(b)):
#     print(*b[i])
suyeol(N,depth)
