"""Class CustomList inherited from built-in class list"""

import functools
from itertools import zip_longest
import operator


class CustomList:
    """Class CustomList"""
    def __init__(self, custom_list=None):
        super().__init__()
        self.custom_list = custom_list

    def __error_catch(func):
        @functools.wraps(func)
        def wrapper(self, other):
            if not isinstance(other, CustomList):
                raise TypeError("Value must be list or CustomList")
            return func(self, other)
        return wrapper

    def arithmetic_operation(self, other, operand: str = '+', first_list_sub_flag: bool = True):
        """Function for arithmetic action"""

        ops = {'+': operator.add,
               '-': operator.sub}

        result = []

        if isinstance(other, CustomList):
            result = [ops[operand](first, second) for first, second
                      in zip_longest(self.custom_list, other.custom_list, fillvalue=0)]
        elif isinstance(other, list):
            result = [ops[operand](second, first) if first_list_sub_flag is False
                      else ops[operand](first, second)
                      for first, second in zip_longest(self.custom_list, other, fillvalue=0)]
        else:
            raise TypeError("Value must be list or CustomList")
        return result

    def __add__(self, other):
        result = self.arithmetic_operation(other, '+')
        return self.__class__(result)

    def __sub__(self, other):
        result = self.arithmetic_operation(other, '-')
        return self.__class__(result)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        result = self.arithmetic_operation(other, '-', False)
        return self.__class__(result)

    @__error_catch
    def __eq__(self, other):
        return sum(self.custom_list) == sum(other.custom_list)

    @__error_catch
    def __ne__(self, other):
        return sum(self.custom_list) != sum(other.custom_list)

    @__error_catch
    def __lt__(self, other):
        return sum(self.custom_list) < sum(other.custom_list)

    @__error_catch
    def __le__(self, other):
        return sum(self.custom_list) <= sum(other.custom_list)

    @__error_catch
    def __gt__(self, other):
        return sum(self.custom_list) > sum(other.custom_list)

    @__error_catch
    def __ge__(self, other):
        return sum(self.custom_list) >= sum(other.custom_list)

    def __str__(self):
        return f"{self.custom_list}, {len(self.custom_list)}"


if __name__ == "__main__":
    custom1 = CustomList([1, 2, 3])
    custom2 = CustomList([1, 9])
    print(custom2 + custom1)
