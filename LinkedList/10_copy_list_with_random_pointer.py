class Node:
    def __init__(self, x, next=None, random=None):
        self.val = x
        self.next = next
        self.random = random


def copy_random_list(head):
    if not head:
        return None

    copies = {}

    curr = head
    while curr:
        copies[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        copies[curr].next = copies.get(curr.next)
        copies[curr].random = copies.get(curr.random)
        curr = curr.next

    return copies[head]
