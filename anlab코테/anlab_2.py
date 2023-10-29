def solution(s):
    n = len(s)
    even_changes = 0
    odd_changes = 0

    for i in range(1, n):
        if i % 2 == 0:
            if s[i] <= s[i - 1]:
                even_changes += s[i - 1] - s[i] + 1
                s[i] = s[i - 1] + 1
        else:
            if s[i] >= s[i - 1]:
                odd_changes += s[i] - s[i - 1] + 1
                s[i] = s[i - 1] - 1
    print(even_changes)
    print(odd_changes)
    return max(even_changes, odd_changes)


# 입력 예시
s = [3, -1, 0, 4]
print(solution(s))  # 출력: 2
