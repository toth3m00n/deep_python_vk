### Метакласс, который в начале названия всех атрибутов и методов, кроме магических, содержит префикс "custom_"
Подменяться должны атрибуты класса и атрибуты экземпляра класса, в том числе добавленные после выполнения конструктора (динамически в природе).

    class CustomMeta(...):
        pass


    class CustomClass(metaclass=CustomMeta):
        x = 50

        def __init__(self, val=99):
            self.val = val

        def line(self):
            return 100

        def __str__(self):
            return "Custom_by_metaclass"


    assert CustomClass.custom_x == 50
    CustomClass.x  # ошибка

    inst = CustomClass()
    assert inst.custom_x == 50
    assert inst.custom_val == 99
    assert inst.custom_line() == 100
    assert str(inst) == "Custom_by_metaclass"

    inst.x  # ошибка
    inst.val  # ошибка
    inst.line() # ошибка
    inst.yyy  # ошибка

    inst.dynamic = "added later"
    assert inst.custom_dynamic == "added later"
    inst.dynamic  # ошибка


### Дескрипторы с проверкой типов и записей данных.

- Я написала реализацию класса Physic: 
```commandline
class Physic:
    """Class Physics - value: name, age, constant of this physics"""

    age = Integer()
    constant = FloatNumberWithPrecision(4)
    name = String()

    def __init__(self, name: str, age: int, constant: (int, float)):
        self.name = name
        self.age = age
        self.constant = constant

    def __str__(self):
        return f"Class of physic {self.name} ( {__class__} )"
```