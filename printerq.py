from typing import List
import collections
from sys import stdin

class Solution:
    def printerQueue(self, docCount: int, docIndex: int, priority: List[int]) -> int:
        printer = collections.deque() #
        for i, p in enumerate(priority):  # N: 4 M: 2 priority: 1, 2, 3,
            printer.append([i, p]) #           (2, 3) (1, 2) (0, 1) (1, 2)
        answer = 0
        while printer:
            i, p = printer.popleft() #어떡할까얘를
            if p == max(priority): # (i = 0) p = 1 != 4 (i = 1) p = 2
                answer += 1 # 1 +
                if i == docIndex:
                    return answer # 1 + 1
                else:
                    priority.remove(p)
            else:
                printer.append([i, p]) #뒤에 붙이는거 잊지말고


for i in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    priority = list(map(int, stdin.readline().split()))
    print(Solution().printerQueue(N, M, priority))

