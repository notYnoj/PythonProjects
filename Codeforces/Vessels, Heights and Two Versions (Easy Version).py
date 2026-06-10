

t = int(input())
while t != 0:
    n = int(input())
    lst = list(map(int, input().split()))
    ret = []
    for pivot in range(n):
        cur = [0] * n
        #ensure cur[pivot] = 0
        #pass left
        i = (pivot - 1) % n
        mx = 0
        while i != pivot:
            mx = max(mx, lst[i])
            cur[i] = mx
            i-=1
            i%=n
        #pass right
        mx = lst[ (pivot) % n]
        i = (pivot + 1) % n
        while i != pivot:
            cur[i] = min(cur[i], mx)
            mx = max(mx, lst[i])
            i+=1
            i%=n
        #sum
        ret.append(sum(cur))
    for item in ret:
        print(item, end = " ")
    t-=1