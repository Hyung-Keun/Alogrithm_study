#Array and linked list
#magic method __init__ working
class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")

rtan = Person("rtanny")
rtan.sayhello("hanghae")

#structure.py 대신 만든부분 연결리스트
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return
        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

lst = [1 ,2 ,3]
l1 = LinkedList()
for e in lst:
    l1.append(e)
print(l1)
