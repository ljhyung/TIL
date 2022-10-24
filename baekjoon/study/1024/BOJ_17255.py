'''
https://www.acmicpc.net/problem/17255
N으로 만들기
골드4
1시간
'''

N = list(map(str, input()))

lenN = dict()    # 그 숫자에 다다르는 방법 수 기록용

def dfs(N):
    if lenN.get(''.join(N)):
        return
    length = len(N)
    if length==1:
        lenN[N[0]]=1
        return
    elif length==2:
        temp = ''.join(N)
        lenN[temp] = len(set(N))
    elif length > 2:
        dfs(N[1:])
        dfs(N[:-1])
        if N[1:]==N[:-1]:
            lenN[''.join(N)] = lenN[''.join(N[1:])]
        else:
            lenN[''.join(N)] = lenN[''.join(N[1:])] + lenN[''.join(N[:-1])]

dfs(N)
print(lenN[''.join(N)])