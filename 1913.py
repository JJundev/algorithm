import sys

n = int(sys.stdin.readline())

rows = n
cols = n
arr = [[0] * cols] * rows
i = 0
j = 0
x_top = n-1
y_top = n-1
x_bottom = 0
y_bottom = 0
m = n**2
while m > 0:
    if i <= x_top:
        for k in range(x_top):
            arr[i][j] = m
            print(i, j, m, "down")
            if i == x_top:
                x_top -= 1
            else:
                i += 1
            m -= 1

    elif j <= y_top:
        arr[i][j] = m
        print(i, j, m, "right")
        if j == y_top-1:
            y_top -= 1
        else:
            j += 1
        m -= 1

    elif i >= x_bottom:
        arr[i][j] = m
        print(i, j, m, "up")
        if i == x_bottom:
            x_bottom += 1
        else:
            i -= 1
        m -= 1

    elif j >= y_bottom:
        arr[i][j] = m
        print(i, j, m, "left")
        if j == y_bottom:
            y_bottom += 1
        else:
            j -= 1
        m -= 1


print(arr)
