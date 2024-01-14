## LRU-кэш
Интерфейс:

    class LRUCache:

        def __init__(self, limit=42):
            ..code

        def get(self, key):
            ..code

        def set(self, key, value):
            ..code
Сложность решения по времени в среднем O(1). Реализация через двусвязанный список,
мапу, которая хранит key-value и мапа, которая хранит key-iterator_in_doublelinkedlist