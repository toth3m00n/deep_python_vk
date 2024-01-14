"""This is homework of descriptors"""


class FloatNumberWithPrecision:
    """FloatNumberWithPrecision descriptor value"""

    @staticmethod
    def verify_value_by_precision(value: (float, int), accuracy: int):
        if isinstance(value, float):
            string_value = str(value)
            if len(string_value) - string_value.index('.') < accuracy:
                raise ArithmeticError(f"You need at least {accuracy} precision for {value}")
        else:
            raise TypeError("Constant have to be integer")

    def __init__(self, accuracy=1):
        self.accuracy = accuracy
        self.constant = 'constant'

    def __get__(self, instance, owner):
        return instance.__dict__[self.constant]

    def __set__(self, instance, value):
        self.verify_value_by_precision(value, self.accuracy)
        instance.__dict__[self.constant] = value


class Integer:
    """Descriptor Integer value"""

    @staticmethod
    def verify_data_by_age(age):

        if not isinstance(age, int):
            raise TypeError("Age have to be integer")

        if not(19 < age < 120):
            raise Exception("Scientists nt be that age! Especially physics")

    def __init__(self):
        self.age = 'age'

    def __get__(self, instance, owner):
        return instance.__dict__[self.age]

    def __set__(self, instance, value):
        self.verify_data_by_age(value)
        instance.__dict__[self.age] = value


class String:
    """Descriptor String value"""

    @staticmethod
    def verify_data_by_name(name: str):
        if not isinstance(name, str):
            raise TypeError
        name_list = name.split()
        if len(name_list) < 2:
            raise Exception('Name of physics have to contain at least Name and Second Name')

    def __init__(self):
        self.name = 'name'

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify_data_by_name(value)
        instance.__dict__[self.name] = value


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


if __name__ == '__main__':
    Plank = Physic('Max Plank', 34, 6.6261)
    Boltzmann = Physic('Ludvig Boltzman', 54, 1.38065)
    Kudrin = Physic('Iaroslav Kudrin', 20, 29.2929)
    print(Plank.__dict__)
    print(Plank)
