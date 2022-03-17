class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None #시작할때 프론트녀석을 만들어주는것이 굉장히 중요하다.

    def is_empty(self): #비었는지 안비었는지 보려면
        return self.front is None #none이면 빈것이고 아니면 안빈것

    def push (self, value): #무언가를 넣어줄땐
        if not self.front: #만약에 이녀석이 비었다면, 새로만든 벨류를 넣어주자.
            self.front = Node(value, None)
            return

        node = self.front #안비었다면,
        while node.next: #계속 끝까지간다.
            node = node.next #다음이 존재하는한 끝까지간다

        node.next = Node(value, None) #while문이 끝났을땐 끝까지 도달한상태이다.
                        #새로만든 노드로 마무리한다.
    def pop(self):#꺼낼땐
        if not self.front: #프론트가 없으면 아무것도 안준다.
            return None

        node = self.front #비지않았다면 제일앞에녀석을꺼낸다
        self.front = self.front.next #기존녀석에 다음녀석을 새로운 프론트로 지정해준 후에
        return node.item #제일앞에녀석꺼내서 노드의 아이템 즉 데이터를 반환하면된다.