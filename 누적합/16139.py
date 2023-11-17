import sys

s = sys.stdin.readline()
q = int(sys.stdin.readline())

for _ in range(q):
    arr = list(map(str, sys.stdin.readline().split()))
    arr[1] = int(arr[1])
    arr[2] = int(arr[2])

    ans = 0
    for i in range(arr[1],arr[2]+1):
        if s[i] == arr[0]:
            ans+=1
    print(ans)