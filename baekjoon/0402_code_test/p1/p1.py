dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]

def sol(n, res):
    for i in range(len(res) - 2):
        if dist[res[i]][res[i + 2]] != dist[res[i]][res[i + 1]] + dist[res[i + 1]][res[i + 2]]:
            return
    if n==len(dist[0]):
        for i in range(len(res) - 2):
            if dist[res[i]][res[i + 2]] != dist[res[i]][res[i + 1]] + dist[res[i + 1]][res[i + 2]]:
                break
        else:
            result.append(res)
        return
    for i in range(len(dist[0])):
        if visited[i]==0:
            visited[i]=1
            sol(n+1, res + [i])
            visited[i]=0

visited = [0]*len(dist[0])
result = []
sol(0, [])

print(result)



