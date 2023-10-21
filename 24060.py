import sys

def merge_sort(arr):
    if len(arr)==1:
        return arr
    
    mid = (len(arr)+1)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    i=0
    j=0
    arr2 =[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr2.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            arr2.append(right[j])
            ans.append(right[j])
            j+=1

    while i<len(left):
        arr2.append(left[i])
        ans.append(left[i])
        i+=1

    while j<len(right):
        arr2.append(right[j])
        ans.append(right[j])
        j+=1

    return arr2

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

ans =[]
arr = merge_sort(arr)

if len(ans)>=k:
    print(ans[k-1])
else:
    print(-1)