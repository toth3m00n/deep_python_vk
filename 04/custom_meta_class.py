"""This is homework of Metaclasses"""


class CustomMeta(type):
    """Metaclass: add custom_ after all attributes and methods"""

    def __new__(cls, name, base, attrs):
        print("__new__ in CustomMeta")
        attrs_with_prefix_custom = {}
        for attr, value in attrs.items():
            if not attr.startswith('__'):
                attrs_with_prefix_custom['custom_' + attr] = value
            else:
                attrs_with_prefix_custom[attr] = value
        return super().__new__(cls, name, base, attrs_with_prefix_custom)


class CustomClass(metaclass=CustomMeta):
    """CustomClass"""

    x = 50

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        return 100

    def __setattr__(self, key, value):
        super().__setattr__('custom_' + key, value)

    def __str__(self):
        return "Custom_by_metaclass"


inst = CustomClass()
print(inst.__dict__)
