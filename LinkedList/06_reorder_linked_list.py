class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    if not head or not head.next:
        return head

    # Find middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    curr = slow.next
    slow.next = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Merge two halves
    first = head
    second = prev

    while second:
        t1 = first.next
        t2 = second.next

        first.next = second
        second.next = t1

        first = t1
        second = t2

    return head
