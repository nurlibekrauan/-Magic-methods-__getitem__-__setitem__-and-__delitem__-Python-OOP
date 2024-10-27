# 18. Магические методы __getitem__, __setitem__ и __delitem__ | ООП Python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        raise IndexError("НЕВЕРНЫЙ ИНДЕКС")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом ")
        if not isinstance(value, int):
            raise TypeError("значение должен быть целым числом")
        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)
        self.marks[key] = value
    def __delitem__(self, key):
        if not isinstance(key,int):
            raise TypeError("Индекс должен быть целым числом")
        
        del self.marks[key]



s1 = Student("Сергей", [5, 5, 3, 2, 5])
try:
    s1[-2] = 4
except Exception as e:
    print(e)
print(s1[2])
try:
    print(s1[10])
except Exception as e:
    print(e)
s1[10] = 4
print(s1.marks)
del s1[2]
print(s1.marks)