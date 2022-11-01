'''
https://school.programmers.co.kr/learn/courses/30/lessons/81303
표 편집
카카오 기출 레벨3

'''

def solution(n, k, cmd):
    answer = ''
    stack = []
    lst = dict()
    for i in range(1,n-1):
        lst[i] = [i-1,i+1,False]
    lst[0] = [-1,1,False]
    lst[n-1] = [n-2,-1,False]

    for i in cmd:
        if i[0]=="D" or i[0]=="U":
            delta, cnt = i.split()
            cnt = int(cnt)
            if delta=='U':
                while cnt:
                    k = lst[k][0]
                    cnt -= 1
            else:
                while cnt:
                    k = lst[k][1]
                    cnt -= 1
        else:
            if i=='C':
                stack.append(k)
                lst[k][2]=True
                prev=lst[k][0]
                next=lst[k][1]
                if next==-1:
                    lst[prev][1]=-1
                    # lst[k][0]=-1
                    k = prev
                elif prev==-1:
                    lst[next][0]=-1
                    # lst[k][1]=-1
                    k=next
                else:
                    lst[prev][1] = next
                    lst[next][0] = prev
                    # lst[k]=[-1,-1,True]
                    k=next

            else:
                recover = stack.pop()
                # lst[recover][2]=False
                prev = recover-1
                if prev<0:
                    prev=-1
                else:
                    while lst[prev][2]:
                        if prev == 0:
                            prev=-1
                            break
                        prev-=1

                next = recover+1
                if next==n:
                    next=-1
                else:
                    while lst[next][2]:
                        next+=1
                        if next==n:
                            next=-1
                            break
                lst[recover]=[prev,next,False]
                if prev!=-1:lst[prev][1] = recover
                if next!=-1:lst[next][0] = recover

    for i in range(n):
        if lst[i][2]:
            answer+="X"
        else:
            answer+="O"

    return answer


print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))