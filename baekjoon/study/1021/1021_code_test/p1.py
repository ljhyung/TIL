def solution(stack1, stack2, stack3):
    res = []
    idxA = len(stack1)-1
    idxB = len(stack2)-1
    idxC = len(stack3)-1
    a = stack1[idxA] if idxA>=0 else 0
    b = stack2[idxB] if idxB>=0 else 0
    c = stack3[idxC] if idxC>=0 else 0

    while idxA>=0 or idxB>=0 or idxC>=0:
        temp = max([a,b,c])
        if temp==a:
            res.append(1)
            idxA -= 1
            if idxA<0:
                a=-1
                continue
            a  = stack1[idxA]

        elif temp==b:
            res.append(2)
            idxB -= 1
            if idxB < 0:
                b = -1
                continue
            B = stack2[idxB - 1]

        elif temp==c:
            res.append(3)
            idxC -= 1
            if idxC < 0:
                c = -1
                continue
            c = stack3[idxC - 1]
    return ''.join(map(str,res))

