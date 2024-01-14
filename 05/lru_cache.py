''' Реализация LRU-cache'''

from doublelinkedlist import DoublyLinkedList


class LRUCache:
    '''Class LRU'''
    def __init__(self, n: int):
        self.HashKeyToValue = {}
        self.HashKeyToIterator = {}
        self.List = DoublyLinkedList()
        self.capacity = n

    def get(self, key):
        ''' Get-method '''
        if key in self.HashKeyToValue:
            list_it = self.HashKeyToIterator[key]
            if list_it is not self.List.return_head_iterator():
                self.List.remove_node(list_it)
                self.List.insert_begin(key)
                self.HashKeyToIterator[key] = self.List.return_head_iterator()
            return self.HashKeyToValue[key]
        return None

    def set(self, key, value):
        '''Set-method'''

        # если ключ уже присутствует в кэше
        if key in self.HashKeyToValue:
            head = self.List.return_head_iterator()

            list_it = self.HashKeyToIterator[key]

            # если он и так самый свежий: то просто обновляем данные
            if list_it is head:
                self.HashKeyToValue[key] = value
                return

            # если нет то сначала удаляем из середины
            self.List.remove_node(list_it)

        # если ключ был встречен в первые (в рамках памяти кэша)
        else:

            # если закончилось место в кэше,
            # то удаляем последний элемент со всех мап и двусвязанного списка
            if self.List.size == self.capacity:
                tail = self.List.return_tail_iterator()
                self.List.remove_end()
                del self.HashKeyToIterator[tail.data]
                del self.HashKeyToValue[tail.data]

        # если все ок или после удаление,
        # то пишем ключ как самый свежей в начало двусвязанного списка
        self.List.insert_begin(key)
        self.HashKeyToValue[key] = value
        self.HashKeyToIterator[key] = self.List.return_head_iterator()


# cache = LRUCache(2)
# cache.set("k1", "val1")
# cache.set("k2", "val2")
# cache.set("k3", "val3")
# cache.set("k4", "val4")
# cache.get("k2")
# cache.get("k4")
# print(cache.HashKeyToValue)
# cache.List.print_list()
# print("d: ", dict(map(lambda kv: (kv[0], kv[1].data), cache.HashKeyToIterator.items())))
