def solution(flowers):
    answer = 0
    day = [0 for _ in range(366)]
    for flower in flowers:
        for d in range(flower[0],flower[1]):
            day[d]+=1
    for i in range(366):
        if day[i]:
            answer+=1
    return answer



print(solution(
[[2, 5], [3, 7], [10, 11]]))

print(solution(
[[3, 4], [4, 5], [6, 7], [8, 10]]))

print(solution([[1,365] for _ in range(100)]))