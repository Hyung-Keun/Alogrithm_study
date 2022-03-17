class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.front = None #제일 앞에있는 것

    def push(self, value):
        if not self.front: #기존에 없으면 넣어준다.
            self.front = Node(value, None) #프론트 넣어준다
            return

        node = self.front #기존에 프론트가 있으면~
        while node.next: #처음에서 제일 끝까지간다음에~
            node = node.next#계속 다음을 향하다가
        node.next = Node(value, None) #끝녀석에 다음을 만들어준다


    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item

    def is_empty(self):
        return self.front is None