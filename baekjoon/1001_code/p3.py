cnt = 0
def solution(k):
    global cnt
    answer = -1

    lst = [6,2,5,5,4,5,6,3,7,6]
    llst = [1,7,4,2,3,5,0,6,9,8]
    visited = [0 for _ in range(k+1)]

    def dfs(k,depth,result):
        global cnt
        if k==0:
            cnt += 1
            # print(result)
            return
        elif k<2:
            return
        if visited[k] and depth!=0:
            cnt += k
            return
        if depth==0:
            if k==6:
                cnt += 1
            for i in range(1,10):
                if lst[i] <= k:
                    dfs(k - lst[i], depth + 1, result+[i])
        else:
            visited[k]=cnt
            for i in range(10):
                if lst[i]<=k:
                    dfs(k-lst[i],depth+1, result+[i])
            visited[k] = cnt-visited[k]


    dfs(k,0,[])
    answer = cnt
    return answer

print(solution(6))