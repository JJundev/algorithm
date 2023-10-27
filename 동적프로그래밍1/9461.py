import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n ==1:
        print(1)
    elif n==2:
        print(1)
    elif n==3:
        print(1)
    elif n==4:
        print(2)
    elif n==5:
        print(2)
    else:
        dp = [0]*(n+1)
        dp[1]=1
        dp[2]=1
        dp[3]=1
        dp[4]=dp[1]+dp[3]
        dp[5]=dp[4]
        for i in range(6,n+1):
            dp[i] = dp[i-5]+dp[i-1]
        print(dp[n])