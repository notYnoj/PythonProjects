t = int(input())
while t != 0:
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    canDo = True
    for i in range(n-2):
        if lst[i] % lst[i+1] != lst[i+2]:
            canDo = False
            break
    if canDo:
        print(f"{lst[0]} {lst[1]}")
    else:
        print(-1)
    t-=1
