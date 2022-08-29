import sys
sys.stdin = open("sample_input.txt", "r")


def dfs(now, depth, cnt, visited):
    global answer
    r,c = now[0], now[1]
    if depth==3:
        answer = max(cnt, answer)
        return
    for dr,dc in [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1]] if c%2 else [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1]]:
        if 0<=r+dr<H and 0<=c+dc<W and visited[r+dr][c+dc]==0:
            visited[r + dr][c + dc]=1
            dfs([r+dr,c+dc],depth+1,cnt+lst[r + dr][c + dc], visited)
            visited[r + dr][c + dc]=0


T = int(input())
for tc in range(1, 1+T):
    W, H = map(int, input().split())
    answer = 0
    lst = [list(map(int, input().split())) for _ in range(H)]
    visit = [[0 for _ in range(W)] for _ in range(H)]
    for r in range(H):
        for c in range(W):
            visit[r][c]=1
            dfs([r,c],0,lst[r][c],visit)
            visit[r][c]=0
    # print(lst)
    print(f'#{tc} {answer**2}')