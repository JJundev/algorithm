import sys

n = int(sys.stdin.readline())
m = list(map(int,sys.stdin.readline().split()))

for i in range(1,n):
    m[i] = max(m[i],m[i]+m[i-1])
print(max(m))