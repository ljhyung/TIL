V = int(input())
E = int(input())
lst = [[] for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
virus = [0]*(V+1)
queue = [1]
while queue:
    num = queue.pop(0)
    virus[num]=1
    for i in lst[num]:
        if virus[i]==0:
            queue.append(i)

print(virus.count(1)-1)
