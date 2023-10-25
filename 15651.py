import sys

n, m = map(int, sys.stdin.readline().split())

s = []


def dfs(j):
    
    if len(s) == m:
        print(' '.join(map(str, s)))
        j += 1
        return
    for i in range(j, n+1):
        s.append(i)
        dfs(i)
        s.pop()

j = 1
dfs(j)
