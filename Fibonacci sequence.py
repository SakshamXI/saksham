def fs(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fs(n-2) + fs(n-1)
n = int(input(" "))
for x in range(1,n+1):
    print(fs(x))
fs(4)

