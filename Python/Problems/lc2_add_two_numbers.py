# 2. Add Two Numbers

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None and l2 is not None:
        return l2
    elif l1 is not None and l2 is None:
        return l1
    elif l1 is None and l2 is None:
        return None

    result = None
    carry = 0
    while l1 is not None or l2 is not None:
        first_data = 0 if l1 is None else l1.val
        second_data = 0 if l2 is None else l2.val
        sum = first_data + second_data + carry
        new_node = ListNode(0)
        if sum < 10:
            new_node.val = sum
            carry = 0
        else:
            new_node.val = sum % 10
            carry = 1

        if result is None:
            result = new_node
            current = result
        else:
            current.next = new_node
            current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    if carry > 0:
        current.next = ListNode(carry)
    return result
