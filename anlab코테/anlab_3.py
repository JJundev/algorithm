def solution(mails, period, k):
    answer = 0

    for i in range(len(mails)-2):
        if (mails[i]+mails[i+1]+mails[i+2]) // period >= k:
            answer += 1

    return answer


mails = [9, 20, 10, 30, 23, 4]
period = 3
k = 20
print(solution(mails, period, k))
