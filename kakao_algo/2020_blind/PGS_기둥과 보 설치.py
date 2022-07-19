'''
PGS
기둥과 보 설치
lv 3

https://school.programmers.co.kr/learn/courses/30/lessons/60061
'''

def solution(n, build_frame):
    answer = [[]]
    wall = [[0]*n for _ in range(n)]
    def sol(frame):
        x,y,a,b = frame
        # 설치
        if b:
            if y!=0 and wall[x][y]==0:
                return
            elif y==0 and a==0:
                wall[x + 1][y] += 0.3
                return
            else:
                # 1 보 0.1
                if a:
                    # 설치 가능 시
                    wall[x][y+1] += 0.1
                # 0 기둥 0.3
                else:
                    wall[x+1][y] += 0.3
                return
        # 삭제
        else:
            # 보
            if a:
                pass
            # 기둥
            else:
                if wall[x+1][y] or wall[x][y+1]
        return
    for frame in build_frame:
        sol(frame)
    return answer


print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
