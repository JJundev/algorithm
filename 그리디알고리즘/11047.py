import sys

n,k = map(int,sys.stdin.readline().split())
arr = []
cnt = 0

for _ in range(n):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)

i = n-1
while i>=0:
    if arr[i]<=k:
        cnt+=k//arr[i]
        k%=arr[i]
    else:
        i-=1
print(cnt)