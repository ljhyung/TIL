'''
https://www.acmicpc.net/problem/1135
뉴스 전하기
골드2
40분
'''

N = int(input())
lst = list(map(int, input().split()))
child =[[] for _ in range(N)]   # 자식 저장용
cost = [0]*N                    # 비용 기록용
if N==1:        # 엣지케이스...
    print(0)
else:
    for i in range(N-1,-1,-1):
        child[lst[i]].append(i)
        if len(child[i])==0:
            cost[i] = 0
        else:
            tempList = [cost[temp] for temp in child[i]]    # 자식들 기록
            tempList.sort(reverse=True)                     # 내림차순 정렬
            tempList = [tempList[i]+i+1 for i in range(len(tempList))]  # 전화거는 시간 포함해서 갱신
            cost[i] = max(tempList)                            # 최댓값 저장
            # cost[i] = max(temp, len(child[i]))              # 모든 자식에게 전화거는 시간이랑 비교
    print(cost[0])
