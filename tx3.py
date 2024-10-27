class Matrix:
    def create_matrix(self, i, j):
        return [[0 for _ in range(j)] for _ in range(i)]

    def validate_item(self, item):
        if (
            not isinstance(item, tuple)
            or len(item) != 2
            or not all(isinstance(i, int) for i in item)
        ):
            raise ValueError("Item must be a tuple of two integers")
        if item[0] < 0 or item[1] < 0:
            raise ValueError("Item coordinates must be non-negative")
        if item[0] >= len(self.matrix) or item[1] >= len(self.matrix[0]):
            raise IndexError("Item coordinates are out of range")

    def validate_value(self, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value < 0:
            raise ValueError("Value must be non-negative")

    def __init__(self, i: int, j: int):
        self.matrix = self.create_matrix(i, j)

    def __getitem__(self, item: tuple):
        self.validate_item(item)
        return self.matrix[item[0]][item[1]]

    def __setitem__(self, item: tuple, value: int):
        self.validate_item(item)
        self.validate_value(value)
        self.matrix[item[0]][item[1]] = value

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])


matrix = Matrix(3, 3)  # Матрица 3x3
matrix[(0, 0)] = 10
matrix[(1, 2)] = 20

print(matrix[(0, 0)])  # Вывод: 10
print(matrix[(1, 2)])  # Вывод: 20

try:
    matrix[(3, 3)] = 30  # Должен выбросить IndexError
except IndexError:
    print("IndexError: Item coordinates are out of range")
print(matrix)
