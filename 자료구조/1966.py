import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    imp = deque()
    cnt = 0
    for i in range(n):
        if i == m:
            imp.append((arr[i], 1))
        else:
            imp.append((arr[i], 0))
    while (sum(item[1] for item in imp) == 1):
        if imp[0][0] == max(item[0] for item in imp):
            imp.popleft()
            cnt += 1
        else:
            tmp = imp[0]
            imp.popleft()
            imp.append(tmp)
    print(cnt)
