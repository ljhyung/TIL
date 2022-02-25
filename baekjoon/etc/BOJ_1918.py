
lst = input()
stack = ['0']
top = 0
result = ''
isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
    '0': -1,            # 인덱스 에러를 피하기 위해 stack[0] = ['0']으로 설정
}
icp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3,
    '0': -1,
}


for i in lst:
    if i == ')':
        while True:
            if stack[top] == '(':
                stack.pop()
                top -= 1
                break
            else:
                result += stack.pop()
                top -= 1
    elif i in icp:
        if icp[i]>isp[stack[top]]:
            stack.append(i)
            top += 1
        else:
            while top>0 and icp[i]<= isp[stack[top]]:
                result += stack.pop()
                top -= 1
            stack.append(i)
            top += 1
    else:
        result += i
while top > 0 :
    result += stack[top]
    top -= 1
print(result)