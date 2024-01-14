import unittest
from custom_meta_class import *
from descriptors import *


class TestAll(unittest.TestCase):


    def setUp(self):
        self.inst = CustomClass()
        self.Plank = Physic('Max Plank', 56, 6.6261)

    def test_Meta(self):
        assert self.inst.custom_x == 50
        assert self.inst.custom_line() == 100
        assert self.inst.custom_val == 99
        assert str(inst) == "Custom_by_metaclass"

        inst.dynamic = "added later"
        assert inst.custom_dynamic == "added later"

    def test_Descriptor(self):
        assert self.Plank.name == 'Max Plank'
        assert self.Plank.age == 56
        assert  self.Plank.constant == 6.6261











