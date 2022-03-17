def isPalindrome(head):
    arr = []

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) > 1:
        if arr.pop(0) != arr.pop():
            return False

    return True