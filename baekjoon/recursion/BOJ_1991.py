
def preorder(S):
    if S:
        print(S, end='')
        preorder(c1[num.index(S)])
        preorder(c2[num.index(S)])

def inorder(S):
    if S:
        inorder(c1[num.index(S)])
        print(S, end='')
        inorder(c2[num.index(S)])

def postorder(S):
    if S:
        postorder(c1[num.index(S)])
        postorder(c2[num.index(S)])
        print(S, end='')


V = int(input())
num = [0]*V
c1 = [0]*V
c2 = [0]*V
for i in range(V):
    p, c11, c22 = map(str, input().split())
    num[i] = p
    if c11!='.':
        c1[i] = c11
    if c22!='.':
        c2[i] = c22

preorder('A')
print()
inorder('A')
print()
postorder('A')
