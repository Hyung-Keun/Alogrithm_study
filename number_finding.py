import sys
import collections
import random

input = sys.stdin.readline
dic = collections.defaultdict(str)
N_number = []
M_number = []

N, M = map(int,input().split())
for i in range(N):
    a = random.randrange(1, 100000)
    N_number.append(a)


for j in range(M):
    b = random.randrange(1, 100000)
    M_number.append(b)


for num in M_number:
    print(1) if num in N_number else print(0)#이거 식 좋은거같다 알아놓자!


