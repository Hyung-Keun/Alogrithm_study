class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            return prev


# None <- 1 2 -> 3 -> 4 -> 5 -> none
# None <- 1 <- 2 3 -> 4 -> 5 -> None
# None <- 1 <- 2 < -3 4 -> 5 -> None
# None <- 1 <- 2 <- 3 <- 4 5 -> None
# None <- 1 <- 2 <- 3 <- 4 <- 5 None