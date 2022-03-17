import collections

class MyStack:
    def __init__(self):
        self.front = collections.deque()

    def push(self, val):
        self.front.append(val)
        for i in range(len(self.front) - 1):
            self.front.append(self.front.popleft())
    def pop(self):
        return self.front.popleft()

    def top(self):
        return self.front[0]

    def empty(self):
        return len(self.front) == 0


#deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.

