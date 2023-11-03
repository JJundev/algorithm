import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum_arr = [0]*(n+1)
for i in range(n):
    sum_arr[i+1] = sum_arr[i] + arr[i]

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(sum_arr[e] - sum_arr[s-1])
