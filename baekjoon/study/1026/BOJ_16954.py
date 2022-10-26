'''
https://www.acmicpc.net/problem/16954
움직이는 미로 탈출
골드3
40분
'''
import copy
from pprint import pprint

lst = [list(input()) for _ in range(8)]

def proceed(lst):
    for i in range(7,0,-1):
        lst[i] = lst[i-1]
    lst[0] = ['.']*8
    newllst = copy.deepcopy(lst)
    return newllst


llst = [copy.deepcopy(lst)]
for _ in range(8):
    llst.append(proceed(lst))
res = 0
# print(len(llst))
def dfs(depth,r,c):
    global res
    if depth==8:
        res = 1
        return
    # 현재 depth의 llst랑 depth+1의 llst를 둘 다 체크해서 살아남을 수 있으면 dfs로 넘기기
    for dr,dc in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1],[0,0]]:
        nr = r+dr
        nc = c+dc
        if nr<0 or nr>=8 or nc<0 or nc>=8:continue
        if llst[depth][nr][nc]=='#' or llst[depth+1][nr][nc]=='#':continue
        dfs(depth+1,nr,nc)

dfs(0,7,0)
# pprint(llst)
print(res)
