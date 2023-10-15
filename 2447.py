import sys


def dp(n):
    if n == 1:
        return (["*"])
    star = []
    arr = dp(n//3)

    for i in arr:
        star.append(i*3)
    for i in arr:
        star.append(i+" "*(n//3) + i)
    for i in arr:
        star.append(i*3)
    return star


n = int(sys.stdin.readline())
arr = dp(n)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print("")
