#체이닝방식, 해쉬테이블
import collections
class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defulatdict(ListNode)

    def put(self, key:int, value:int) -> int:
        index = key % self.size
        if self.table[index].value is None:  #만약에 해쉬테이블안에 인덱스값을 가진 값들이 없을때
            self.table[index] = ListNode(key, value) #그냥 빈 리스트노드로 저장한다. 존재하지않는 인덱스 나중에 조회할경우 바로 빈 리스트노드 나올것이다.
            return

        p = self.table[index] #그렇지않고 해쉬테이블안에 인덱스값에 밸류가 있을경우, 노드가 존재하는경우
        while p: #p는 인덱스의 첫번째값이고, 계속 탐색한다. p.next를
            if p.key == key: #이미 키가 존재할경우, 값을 업데이트하고 빠겨나가는 경우.
                p.value = value
                return
            if p.next is None: #다음노드 없으면 아무것도 하지않고 루프를 빠져나간다.
                break
                p = p.next
            p.next = ListNode(key, value) #여기까지 진행되면 새로운 노드를 생성해줄것이고, 연결할것이다. 이것이 개별체이닝방식.

    def get(self, key:int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1 #만약에 해당 인덱스에 아무것도 없으면 이거를 반환한다.

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1


    def remove(self, key:int) ->None:
        index = key % self.sizeif
        if self.table[index].value is None:
            return

        p= self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next #애초에 self.table[index]
            # 이거는 빈 노드이기때문에, 매번 빈 것을 생성하기 때문에 self.table[index]자체를 None으로해버리면 오류발생할것이다
            return
        #현재노드를 이전과 다음노드로부터 끊어버리기 삭제해야되니까...
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


