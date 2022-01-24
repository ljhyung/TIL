N = int(input())
cnt = 0
for i in range(1,N+1):
    i =  list(map(int, str(i)))
    for j in range(len(i)-2):
        if (j[i]-j[i+1]) == (j[i+1]-j[i+2]):
            break
    cnt +=1
print(cnt)
