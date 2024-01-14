''' модуль с тестировванием '''

import unittest
from lru_cache import *

class TestAll(unittest.TestCase):

    def setUp(self):
        self.cache = LRUCache(2)

    def test_set(self):
        ''' проверка установки и обновления значения '''

        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        assert self.cache.HashKeyToValue["k1"] == "val1"
        assert self.cache.HashKeyToValue["k2"] == "val2"

        self.cache.set("k3", "val3")
        assert "k1" not in self.cache.HashKeyToValue
        assert self.cache.HashKeyToValue["k3"] == "val3"

    def test_get(self):
        ''' проверка получаемого значения'''

        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")

        assert self.cache.get("k2") == "val2"
        assert self.cache.get("k3") == "val3"
        assert self.cache.get("k1") is None

        self.cache.set("k4", "val4")
        assert self.cache.get("k4") == "val4"
        assert self.cache.get("k2") is None

        self.cache.set("k1", "val1.2")
        assert self.cache.get("k1") == "val1.2"

    def test_update_cache(self):
        ''' проврека обновления кэша'''

        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

        assert self.cache.HashKeyToIterator["k2"] == self.cache.List.return_head_iterator()

        self.cache.set("k1", "val1.2")
        assert self.cache.HashKeyToIterator["k1"] == self.cache.List.return_head_iterator()
