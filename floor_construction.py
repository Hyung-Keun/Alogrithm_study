import sys

input = sys.stdin.readline
d = [[0] for _ in range(250)]
d[0] = 1
d[1] = 3
for i in range(2, 250):
    d[i] = d[i - 1] + d[i - 2] * 2
while True:
    try:
        n = int(input().rstrip())
        if n == 0:
            print(1)
        else:
            print(d[n - 1])
    except:
        break
