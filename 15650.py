import sys

n, m = map(int, sys.stdin.readline().split())

s = []
visited = [False]*(n+1)

j = 1


def dfs(j):

    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(j, n+1):
        if visited[i]:
            continue
        visited[i] = True
        j += 1

        s.append(i)
        dfs(j)
        s.pop()
        visited[i] = False


dfs(j)
