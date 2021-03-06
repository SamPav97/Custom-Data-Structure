from copy import deepcopy


class NoElementsInListError(Exception):
    pass


class NoSuchValueError(Exception):
    pass


class CustomIntList:
    def __init__(self):
        self.__values = []

    def append(self, val):
        if not isinstance(val, int):
            raise ValueError("Only ints are accepted")

        self.__values.append(val)

    def remove(self, index):
        try:
            el = self.__values.pop(index)
            return el
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer. Please pass an integer number")

    def get(self, index):
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError("Invalid index")

    def extend(self, vals):
        try:
            for el in vals:
                if not isinstance(el, int):
                    raise ValueError("Only ints are accepted")
            self.__values.extend(vals)
            return deepcopy(self.__values)
        except TypeError:
            raise ValueError("Extend method works only with iterable objects")

    def insert(self, index, v):
        try:
            if index < 0 or index >= len(self.__values):
                raise IndexError
            self.__values.insert(index, v)
            return self.__values
        except IndexError:
            raise IndexError("Invalid index")
        except TypeError:
            raise ValueError("Index is not a valid integer. Please pass an integer number")

    def pop(self):
        if not self.__values:
            raise NoElementsInListError("No Elements in list")
        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index_left(self, value):
        try:
            return self.__values.index(value)
        except ValueError:
            raise NoSuchValueError("No such value in the list")

    def index_right(self, value):
        for index in range(len(self.__values) - 1, -1, -1):
            if self.__values[index] == value:
                return index
        raise NoSuchValueError("No such value in the list")

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, val):
        if not isinstance(val, int):
            raise ValueError("Only ints are accepted")
        self.__values.insert(0, val)

    def dictionize(self):
        result = {}
        for index in range(0, len(self.__values), 2):
            key = self.__values[index]
            try:
                value = self.__values[index+1]

            except IndexError:
                value = " "

            result[key] = value
        return result

    def move(self, n):
        self.__values = self.__values[n:] + self.__values[:n]
        return self.__values

    def sum(self):
        # If our list accepts other values than ints we can sum like follows
        # res = 0
        # for el in self.__values:
        #     if isinstance(el, int) or isinstance(el, float):
        #         res += el
        #     else:
        #         res += len(el)
        # return res
        return sum(self.__values)

    def overbound(self):
        return max(self.__values)
    # I need to create an algorythm if not all values are ints.

    def underbound(self):
        return min(self.__values)
    # Ibid.

