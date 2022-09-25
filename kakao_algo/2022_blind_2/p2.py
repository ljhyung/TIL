def solution(cap, n, deliveries, pickups):
    answer = 0
    phead = n - 1
    dhead = n - 1
    while True:
        dis = 0
        nowput = cap
        nowpull = 0
        for i in range(phead,-1,-1):
            if pickups[i]!=0:
                dis = max(dis, i + 1)
                for j in range(dhead,-1,-1):
                    if deliveries[j]!=0 and nowput!=0:
                        dis = max(dis, j+1)
                        if deliveries[j]<=nowput:
                            nowput -= deliveries[j]
                            deliveries[j]=0
                            dhead = j-1
                        else:
                            deliveries[j]-=nowput
                            nowput=0
                            break
                if pickups[i]>cap-nowpull:
                    pickups[i]-=(cap-nowpull)
                    break
                else:
                    nowpull+=pickups[i]
                    pickups[i]=0
                    phead = i-1
        answer += dis * 2
        if(sum(deliveries)+sum(pickups)==0):break

    return answer


print(solution(
4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))