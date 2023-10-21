import sys

def h(n,start,end):
    if n==1:
        print(start,end)
    else:
        h(n-1,start,6-start-end)
        print(start,end)
        h(n-1,6-start-end,end)
def hc(n):
    if n==1:
        return 1
    else:
        return hc(n-1)*2+1

n = int(sys.stdin.readline())
a = 1
print(hc(n))
h(n,1,3)