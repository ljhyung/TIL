'''
성격유형검사 동의부터 비동의까지 7단계
'''

def solution(survey, choices):
    answer = ''
    res = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }
    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]
        if choices[i]==4:
            continue
        elif choices[i]<4:
            res[a] += (4-choices[i])
        else:
            res[b] += choices[i]-4
    if res['R']<res['T']:
        answer += 'T'
    else:
        answer += 'R'
    if res['C']<res['F']:
        answer += 'F'
    else:
        answer += 'C'
    if res['J']<res['M']:
        answer += 'M'
    else:
        answer += 'J'
    if res['A']<res['N']:
        answer += 'N'
    else:
        answer += 'A'


    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))