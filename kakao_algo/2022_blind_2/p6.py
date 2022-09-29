from collections import deque


def solution(n, m, x, y, r, c, k):
    answer = ''
    tempanswer = ''
    x-=1
    y-=1
    r-=1
    c-=1
    def bfs():
        global answer
        queue = deque()
        queue.append([r,c,0,[]])
        while queue:
            rr,cc,dis,path = queue.popleft()
            if rr==r and cc==c and dis==k-len(tempanswer):

                return ''.join(path)
            if dis==k:
                continue
            for delta in ['d', 'l', 'r', 'u']:
                nr = rr+dir[delta][0]
                nc = cc+dir[delta][1]
                if 0<=nr<n and 0<=nc<m:
                    if dis+1<=k-len(tempanswer):
                        queue.append([nr,nc,dis+1,path+[delta]])

    if((abs(x-r)+abs(y-c))%2!=k%2):
        return "impossible"
    if((abs(x-r)+abs(y-c))>k):
        return "impossible"
    if(x-r<0):
        tempanswer += 'd'*abs(x-r)
    if(y-c>0):
        tempanswer += 'l'*abs(y-c)
    if (y - c < 0):
        tempanswer += 'r' * abs(y - c)
    if(x-r>0):
        tempanswer += 'u'*abs(x-r)

    # print(tempanswer)
    dir = {
        'd' : [1,0],
        'l' : [0,-1],
        'r' : [0,1],
        'u' : [-1,0]
    }
    lst = [[0 for _ in range(m)] for _ in range(n)]

    if k>len(tempanswer):
        answer = tempanswer + bfs()
    else:
        answer = tempanswer

    return answer

print(solution(3, 4, 2, 3, 3, 1, 5))