class MyCircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.maxlen = k # k: 최대길이
        self.p1 = 0 # front
        self.p2 = 0 #rear

    def enQueue(self, value): #rear 포인터 이동
        if self.q[self.p2] is None:  # rear가 비어있으면~
            self.q[self.p2] = value #끝에 데이터 넣어주고
            self.p2 = (self.p2 + 1) % self.maxlen #한칸 앞으로 가는데 최대길이(maxlen) 안넘도록 한다
            return True
        else:
            return False #끝에 뭐 있으면 말고~

    def deQueue(self): #front 포인터 이동
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None #프론트 비워주고
            self.p1 = (self.p1 + 1) % self.maxlen #한칸 앞으로 이동한후에 최대길이 지켜준다
            return True

    def front(self):
        return -1 if self.q[self.p1] is None else self.q[self.p1] #만약 아무것도 없으면 -1 이상한 놈이니까
        #만약에 프론트 아무것도 없으면,, 그리고 뭔가있다? 그값 보여준다.

    def Rear(self):
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]  # 만약 아무것도 없으면 -1 이상한 놈이니까

    def isEmpty(self):
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        return self.p1 == self.p2 and self.q[self.p1] is not None


