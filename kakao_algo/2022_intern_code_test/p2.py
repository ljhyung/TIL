'''
큐 최소로 움직여서 두 합 같게
'''
def pushpop(n, sum1, sum2):
    global resmin, answer, queue11, queue22
    if resmin:
        return
    if sum1==sum2:
        resmin = True
        answer = n
        return
    # if (sum1+(i-n)*maxnum<half) or (sum2+(i-n)*maxnum)<half:
    #     return
    if resmin==False:
        if queue11:
            a = queue11.pop(0)
            queue22.append(a)
            pushpop(n+1, sum1-a, sum2+a)
            a = queue22.pop(-1)
            queue11 = [a] + queue11

        if queue22:
            a = queue22.pop(0)
            queue11.append(a)
            pushpop(n+1, sum1+a, sum2-a)
            a = queue11.pop(-1)
            queue22 = [a] + queue22
    return

def solution(queue1, queue2):
    global maxnum, half, queue11, queue22, answer
    queue11, queue22 = queue1, queue2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    half = int((sum1+sum2)/2)
    maxnum = max(max(queue1),max(queue2))
    pushpop(0, sum1, sum2)
    return answer

queue11, queue22 = [], []
half = 0
maxnum = 0
answer = -1
resmin = False
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))