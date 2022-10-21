import heapq
from collections import defaultdict


def solution(S, C):
    word = defaultdict(int)
    heap = []
    check = [0 for _ in range(len(S))]
    for i in range(len(S)):
        if word[S[i]]==0:
            if i==1 and S[0]==S[1]:
                heapq.heappush(heap,[0,1])
                word[S[i]] = i
            else:
                word[S[i]]=i
        else:
            heapq.heappush(heap,[word[S[i]],i])
            word[S[i]] = i

    if len(heap)==0:
        return 0
    def addOne(n):
        return n+1
    N = len(heap)
    for i in range(N):
        s,e = heap[i]
        check[s:e] = list(map(addOne,check[s:e]))
    print(heap)
    print(check)
    for i in range(len(C)):
        sit = C[i]-1
        N -= check[sit]
        if N<=0:
            return i+1
    return -1



print(solution('aabcddcb', [3, 5, 1, 4, 7]))
