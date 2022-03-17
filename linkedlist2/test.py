from linkedlist2.prac import isPalindrome
from linkedlist2.structure import LinkedList

l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)

assert isPalindrome(l1.head)
assert not isPalindrome(l2.head)