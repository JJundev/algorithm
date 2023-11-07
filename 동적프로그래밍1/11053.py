import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt = [1]*n

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            cnt[i] = max(cnt[i],cnt[j]+1)

print(max(cnt))