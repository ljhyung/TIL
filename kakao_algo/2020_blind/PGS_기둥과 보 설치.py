'''
PGS
기둥과 보 설치
lv 3

https://school.programmers.co.kr/learn/courses/30/lessons/60061
'''
from pprint import pprint


def solution(n, build_frame):
    answer = []
    wall = [[0]*(n+1) for _ in range(n+1)]
    def sol(frame):
        y,x,a,b = frame
        # 설치
        if b:
            # if x!=0 and wall[x-1][y]==0:
            #     return
            if x==0 and a==0:
                wall[x][y] |= 2
                return
            elif not a and (wall[x-1][y]&2 or (wall[x][y-1]&1 or wall[x][y+1]&1)):
                # # 1 보 01
                # if a:
                #     # 설치 가능 시
                #     wall[x][y] |= 1
                # # 0 기둥 10
                # else:
                wall[x][y] |= 2
                return
            elif a and (wall[x-1][y]&2 or wall[x-1][y+1]&2 or(wall[x][y-1]&1 and wall[x][y+1]&1)):
                wall[x][y] |= 1
                return
            else:
                return
        # 삭제
        else:
            # 보 삭제 조건 XOR ^
            # 1 양 옆으로 보가 있는데 바쳐주는 기둥이 없을 때
            # 2 양 옆으로 위에 기둥이 있는데 바치는 기둥이나 보가 없을 때
            if a:
                if (wall[x][y+1]&1 and (not wall[x-1][y+1]&2 and not wall[x-1][y+2]&2)):
                    return
                if (wall[x][y -1] & 1 and (not wall[x - 1][y - 1] & 2 and not wall[x - 1][y - 2] & 2)):
                    return
                if (wall[x][y]&2 and (not wall[x-1][y]&2 or wall[x][y-1]&1)):
                    return
                if (wall[x][y+1]&2 and (not wall[x-1][y+1]&2 or wall[x][y+1]&1)):
                    return
                wall[x][y] ^= 1
                return
            # 기둥 삭제 조건 1
            else:
                if (wall[x+1][y]&1 and (not wall[x][y+1]&2 and not wall[x+1][y+1]&1)):
                    return
                if (wall[x+1][y-1]&1 and (not wall[x][y-1]&2 and not wall[x+1][y-2]&1)):
                    return
                if wall[x+1][y]&2 and (not wall[x+1][y]&1 or not wall[x+1][y-1]&1):
                    return
                wall[x][y] ^= 2
        return
    for frame in build_frame:
        sol(frame)
    for c in range(n+1):
        for r in range(n+1):
            if wall[r][c]&1:
                answer.append([c,r,1])
            elif wall[r][c]&2:
                answer.append([c,r,0])
    # pprint(wall)
    return answer


print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
print(solution(5, [[0,0,0,1],[0,1,1,1],[0,1,0,1],[0,1,1,0]]))
