import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

tmp = 0
for i in range(k):
    tmp += arr[i]
ans = []
ans.append(tmp)

for i in range(n-k):
    tmp = tmp + arr[i+k] - arr[i]
    ans.append(tmp)

print(max(ans))