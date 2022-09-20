def solution(survey, choices):
    answer = ''
    mbti = {
        "R":0,
        "T":0,
        "C":0,
        "F":0,
        "J":0,
        "M":0,
        "A":0,
        "N":0,
         }

    for i in range(len(survey)):
        a = survey[i][0]
        b = survey[i][1]
        num = choices[i]
        if(num<4):
            mbti[a] += abs(num-4)
        else:
            mbti[b] += abs(num-4)

    answer += "R" if mbti["R"]>=mbti["T"] else "T"
    answer += "C" if mbti["C"]>=mbti["F"] else "F"
    answer += "J" if mbti["J"]>=mbti["M"] else "M"
    answer += "A" if mbti["A"]>=mbti["N"] else "N"
    print(answer)
    return answer


solution(["AN", "CF", "MJ", "RT", "NA"]	,[5, 3, 2, 7, 5])