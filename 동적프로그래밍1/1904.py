import sys
n = int(sys.stdin.readline())

a1 = 1
a2 = 2
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 15746
    print(dp[n])
