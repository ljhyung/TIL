def solution(numbers):
    answer = []

    def cut(num):
        numlen = len(num)
        if numlen==3:
            if num[1]!='0':
                return True
            else:
                return False
        if int(num[:numlen//2])==0:
            left = True
        else:
            left = cut(num[:numlen//2])
        mid = num[numlen//2]
        if int(num[numlen//2+1:])==0:
            right = True
        else:
            right = cut(num[numlen//2+1:])
        if(left and mid!='0' and right):
            return True
        # elif()
        else:
            return False

    for num in numbers:
        if num<=3:
            answer.append(1)
            continue
        binum = bin(num)[2:]
        a=0
        cnt = 0
        while True:
            a += 2**cnt
            cnt += 1
            if a>=len(binum):
                break
        while True:
            if a>len(binum):
                binum = '0' + binum
            else:
                break
        # print(binum)
        answer.append(1 if cut(binum) else 0)


    return answer

print(solution([129]))

# 010000001
# 000000000001111 0 1000010 0 100 0 000