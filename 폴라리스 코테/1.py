import sys


def solution(attackMin, attackMax, damageMin, damageMax, requiredPrice):
    answer = True
    bp = True
    for i in range(attackMin, attackMax+1):
        for j in range(damageMin, damageMax+1):
            if i/j == float(requiredPrice):
                answer = True
                bp = False
        if bp == False:
            break

    if bp == True:
        answer = False
    return answer


a, b, c, d, e = map(int, sys.stdin.readline().split())
print(solution(a, b, c, d, e))

