''' Реализация двусвязанного списка'''

class Node:

    def __init__(self, data: int, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def _insert_to_empty(self, data):
        self._head = Node(data)
        self._tail = self._head
        self.size += 1

    def insert_begin(self, data: int):
        if self._head is None:
            self._insert_to_empty(data)
            return
        _current = Node(data, None, self._head)
        self._head.prev = _current
        self._head = _current
        self.size += 1

    def insert_end(self, data: int):
        if self._tail is None:
            self._insert_to_empty(data)
            return
        _current = Node(data, self._tail, None)
        self._tail.next = _current
        self._tail = _current
        self.size += 1

    def remove_node(self, current: Node):
        if self._head is None:
            return
        if self._head is self._tail:
            self._head = None
            self._tail = None
        else:
            previous = current.prev
            next = current.next
            if next is not None:
                next.prev = previous
            else:
                self._tail = previous
            if previous is not None:
                previous.next = next
            else:
                self._head = next
        self.size -= 1

    def remove_begin(self):
        self.remove_node(self._head)

    def remove_end(self):
        self.remove_node(self._tail)

    def return_tail_iterator(self):
        return self._tail

    def return_head_iterator(self):
        return self._head

    def return_iterator(self, key):
        _current = self._head
        while _current.data != key:
            _current = _current.next
        return _current

    def print_list(self):
        current = self._head
        while current is not None:
            print(current.data, end='⥦')
            current = current.next
        print('None')


# dl = DoublyLinkedList()
# d = {}
# for i in range(3):
#     dl.insert_end(i)
#     d[i] = dl.return_tail_iterator().data
# dl.print_list()
# print(d)
