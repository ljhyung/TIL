import sys
sys.stdin = open("input.txt", "r")

def get_char(T):
    if str.isdigit(T):
        return int(T)
    else:
        return T


def post_order(T):
    if T and type(lst[T][1])==int:  # 리프인 경우
        return lst[T][1]
    elif T:
        a = post_order(lst[T][2])   # 계산인 경우
        b = post_order(lst[T][3])
        return cal[lst[T][1]](a, b) # 계산


cal = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: x-y,
    '*': lambda x,y: x*y,
    '/': lambda x,y: x/y,
}

T = 10
for tc in range(1, T+1):
    V= int(input())
    lst = [[] for _ in range(V+1)]
    for i in range(1, V+1):
        lst[i] = list(map(get_char, input().split()))   # map에 사용자함수 넣어보기 처음 해봅니다
    result = int(post_order(1))
    print(f'#{tc} {result}')