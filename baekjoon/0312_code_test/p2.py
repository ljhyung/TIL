N = int(input())      # 2번 회오리로 숫자 채우기
def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    print(answer)
    dr1 = [0, 1, 0, -1]  # cl 우하좌상
    dc1 = [1, 0, -1, 0]
    dr2 = [1, 0, -1, 0]  # ccl 하우상좌
    dc2 = [0, 1, 0, -1]
    st1 = [0,0]
    st2 = [0, n-1]
    cnt = 1
    delta = 0

    while answer[(n-1)//2][(n-1)//2]==0:
        answer[st1[0]][st1[1]] = cnt
        answer[n-1-st1[0]][n-1-st1[1]] = cnt
        answer[st2[0]][st2[1]] = cnt
        answer[n-1-st2[0]][n-1-st2[1]] = cnt
        if clockwise:
            nst1r = st1[0] + dr1[(delta)%4]
            nst1c = st1[1] + dc1[(delta)%4]
            nst2r = st2[0] + dr1[(delta+1)%4]
            nst2c = st2[1] + dc1[(delta+1)%4]
        else:
            nst1r = st1[0] + dr2[(delta) % 4]
            nst1c = st1[1] + dc2[(delta) % 4]
            nst2r = st2[0] + dr2[(delta - 1) % 4]
            nst2c = st2[1] + dc2[(delta - 1) % 4]
        if 0<=nst1r<n and 0<=nst1c<n and answer[nst1r][nst1c]==0:
            st1[0] = nst1r
            st1[1] = nst1c
            st2[0] = nst2r
            st2[1] = nst2c
            cnt += 1
        else:
            delta += 1
    # answer = [[]]
    return answer

a = solution(N, True)
print(a)



