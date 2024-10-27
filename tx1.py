class Inventory:
    def __init__(self):
        # Инвентарь создается как экземплярный атрибут
        self.inventory = {}

    def validate_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Название товара должно быть строкой")

    def validate_value(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество товара должно быть числом")
        if value < 0:
            raise ValueError("Количество товара не может быть отрицательным")

    def __getitem__(self, key):
        self.validate_key(key)
        # Если товар не найден, лучше вызывать KeyError
        if key in self.inventory:
            return self.inventory[key]
        raise KeyError(f"Товар '{key}' не найден в инвентаре")

    def __setitem__(self, key, value):
        self.validate_key(key)
        self.validate_value(value)
        # Здесь можно обновлять количество товара, а не добавлять только новый
        self.inventory[key] = value

    def __delitem__(self, key):
        self.validate_key(key)
        if key in self.inventory:
            del self.inventory[key]
        else:
            raise KeyError(f"Товар '{key}' не найден в инвентаре")

    def __str__(self):
        return str(self.inventory)

# Пример использования:
inv = Inventory()

# Добавляем товары
inv["яблоки"] = 10
inv["бананы"] = 5

# Получаем количество товара
print(inv["яблоки"])  # 10

# Обновляем количество товара
inv["яблоки"] = 15
print(inv["яблоки"])  # 15

# Удаляем товар
del inv["бананы"]

# Печатаем текущий инвентарь
print(inv)  # {'яблоки': 15}
