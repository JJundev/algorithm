def solution(envelopers):
    mini = []
    envelopers.sort(key=lambda x: (-x[0], -x[1]))
    for i in range(len(envelopers)):
        if envelopers[i] in mini:
            continue
        else:
            for j in range(i+1, len(envelopers)):
                if envelopers[j] in mini:
                    continue
                else:
                    if envelopers[i][0] > envelopers[j][0] and envelopers[i][1] > envelopers[j][1]:
                        mini.append(envelopers[j])
    answer = len(envelopers) - len(mini)
    print(len(mini))
    return answer


envelopers = [[3, 5], [7, 5], [3, 3], [2, 1]]
print(solution(envelopers))
