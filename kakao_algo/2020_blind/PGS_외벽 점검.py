'''
PGS
외벽 점검
lv 3

https://school.programmers.co.kr/learn/courses/30/lessons/60062
'''

def solution(n, weak, dist):
    answer = 0
    visited = [0 for _ in range(n)]
    def sol(d):
        if d==len(dist):
            if weak:
                answer=-1
                return
            else:
                return d
        if not weak:
            return d
        for i in range(len(weak)):
            if visited[i]==0:
                for j in range(len(weak)):

        return
    sol(0)
    return answer


print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))