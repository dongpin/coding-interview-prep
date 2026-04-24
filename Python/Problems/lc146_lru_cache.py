# 146. LRU Cache


class Node:
    def __init__(self):
        self.key = None
        self.value = None
        self.prev = None
        self.next = None


class LRUCache:

    '''
    def __init__(self, capacity: int):
        self.nums = OrderedDict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self.nums:
            return -1
        self.nums.move_to_end(key)
        return self.nums[key]

    def put(self, key: int, value: int) -> None:
        if key in self.nums:
            self.nums.move_to_end(key)
        self.nums[key] = value
        if len(self.nums) > self.capacity:
            self.nums.popitem(last=False)
    '''

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next = node
        node.next.prev = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _pop(self):
        res = self.tail.prev
        self._remove(res)
        return res

    def _move_to_head(self, node):
        self._remove(node)
        self._add(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = Node()
            node.key = key
            node.value = value
            self.cache[key] = node
            self._add(node)
            self.size += 1
        else:
            self._move_to_head(self.cache[key])
            self.cache[key].value = value

        if self.size > self.capacity:
            node = self._pop()
            del self.cache[node.key]
            self.size -= 1
