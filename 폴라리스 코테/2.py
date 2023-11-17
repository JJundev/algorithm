import sys



def solution(bruce, demian):
    answer = []
    for i in range(len(bruce)-1):
        for j in range(i+1,len(bruce)):
            if bruce[i]+bruce[j] > demian[i]+demian[j]:
                if (bruce[i], bruce[j]) in answer or (bruce[j], bruce[i]) in answer:
                    pass
                else:
                    answer.append([bruce[i], bruce[j]])

    return(len(answer))

bruce = list(map(int, sys.stdin.readline().split()))
demian = list(map(int, sys.stdin.readline().split()))

print(solution(bruce, demian))