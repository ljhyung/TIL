def solution(users, emoticons):
    answer = [0,0]
    answerList = []

    def dfs(depth, emoticon):
        if depth == len(emoticons):

            userbuy = [0 for _ in range(len(users))]
            answerList.append([0,0])
            for j in range(len(users)):
                for emo in emoticon:
                    if emo[0]>=users[j][0]:
                        userbuy[j] += emo[1]

                if users[j][1]<=userbuy[j]:
                    answerList[-1][0]+=1
                else:
                    answerList[-1][1] += userbuy[j]

            return
        for i in range(4):
            emoticon[depth][1] = int(emoticons[depth] * (10-(i+1))/10)
            emoticon[depth][0] = (i+1)*10
            dfs(depth+1, emoticon)
    tempemo = []
    for i in range(len(emoticons)):
        tempemo.append([0,emoticons[i]])
    dfs(0,tempemo)
    # answer = answerList.sort(key=lambda x:(x[0], x[1]), reverse=True)
    answer = sorted(answerList,key=lambda x:(x[0], x[1]), reverse=True)

    return answer[0]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))