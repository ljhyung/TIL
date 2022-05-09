from collections import deque


def pushpop(i,n, sum1, sum2):
    global resmin, queue11, queue22
    if n==i:
        if sum1==sum2:
            resmin = True
        return
    if (sum1+(i-n)*maxnum)<half or (sum2+(i-n)*maxnum)<half:
        return
    if resmin==False:
        if queue11:
            a = queue11.popleft()
            queue22.append(a)
            pushpop(i, n+1, sum1-a, sum2+a)
            a = queue22.pop()
            queue11.appendleft(a)

        if queue22:
            a = queue22.popleft()
            queue11.append(a)
            pushpop(i, n+1, sum1+a, sum2-a)
            a = queue11.pop()
            queue22.appendleft(a)
    return

def solution(queue1, queue2):
    global maxnum, half, queue11, queue22
    queue11 = deque(queue1)
    queue22 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = int((sum1+sum2)/2)
    maxnum = max(max(queue1),max(queue2))
    answer = -1
    i=0
    while True:
        if i==2*len(queue11):
            i=-1
            break
        if (sum1 - sum(queue1[0:i - 1])) > half or (sum2 - sum(queue2[0:i - 1])) > half:
            i += 1
            continue
        pushpop(i, 0, sum1, sum2)
        if resmin:
            break
        i += 1
    answer = i
    return answer

queue11 = deque()
queue22 = deque()
half = 0
maxnum = 0
resmin = False


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))