'''
BOJ
DSLR
골드 5

https://www.acmicpc.net/problem/9019
'''
from collections import deque


def bfs(s,e):
    queue = deque()
    queue.append((s,0,[0]))
    while queue:
        lst,cnt,res = queue.popleft()
        if lst == e:
            return res
        temp = lst[:]
        # 1 *2
        num = list(str((int(''.join(temp))*2)%10000))
        while len(num) < 4:
            num = [0] + num
        queue.append((num,cnt+1,res+['D']))
        # 2 -1
        num = int(''.join(temp))-1
        queue.append((list(str(num)) if num else list('9999'), cnt+1, res+['S']))
        # 3 ->
        a = temp.pop(0)
        temp.append(a)
        queue.append((temp[:], cnt+1, res+['L']))
        a = lst.pop(-1)
        lst = [a]+lst
        queue.append((lst, cnt + 1, res + ['R']))




t = int(input())
for _ in range(t):
    S,E = input().split()
    S, E = list(S), list(E)
    while len(S)<4:
        S = [0]+S
    while len(E)<4:
        E = [0]+E
    res = bfs(S,E)
    print(''.join(res[1:]))