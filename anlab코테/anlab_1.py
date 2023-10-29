import sys


def solution(user_times, T):
    min = []
    for i in range(len(user_times)):
        while user_times[i] > T:
            user_times[i] -= T
        min.append(T-user_times[i])
    answer = max(min)
    return answer


# user_times = [20, 40, 65, 110]
user_times = [20, 40, 65, 110]
T = 1
print(solution(user_times, T))
