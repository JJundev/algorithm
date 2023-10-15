T = int(input())

for _ in range(T):
    N = int(input())
    li = list(map(int, input().split()))

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        for j in range(i + 1):
            top = dp[i - 1][j - 1] + li[j - 1] * i
            bottom = dp[i - 1][j] + li[-(i - j)] * i
            dp[i][j] = max(top, bottom)

    print(max(dp[N]))