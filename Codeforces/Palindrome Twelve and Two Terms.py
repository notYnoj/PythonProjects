t = int(input())
for i in range(t):
    n = int(input())
    if n == 10:
        print(-1)
        continue
    rem = n % 12
    if rem == 10:
        print(f"22 {n - 22}")
    else:
        print(f"{rem} {n-rem}")


