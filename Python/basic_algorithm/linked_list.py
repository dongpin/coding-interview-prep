# Node for linked list
#

class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None


class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.head = DoublyNode(-1)
        self.tail = self.head
