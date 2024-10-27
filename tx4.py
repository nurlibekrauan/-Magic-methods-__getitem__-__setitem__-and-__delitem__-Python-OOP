class BoundedList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def __len__(self):
        return len(self.data)

    def validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            raise IndexError("Index must be positive")
        if index >= self.max_size:
            raise OverflowError("Index must be less than max_size")

    def __getitem__(self, index):
        self.validate_index(index)
        return self.data[index]

    def __setitem__(self, index, value):
        self.validate_index(index)
        if value in self.data:
            self.data[index] = value
            return
        self.data.append(value)

    def __delitem__(self, index):
        del self.data[index]

    def __str__(self) -> str:
        return str(self.data)


bounded_list = BoundedList(max_size=3)
bounded_list[0] = "a"
bounded_list[1] = "b"
bounded_list[2] = "c"

print(bounded_list[1])  # Вывод: b
try:
    bounded_list[3] = "d"  # Должен выбросить OverflowError
except OverflowError as e:
    print(e)
