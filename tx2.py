from datetime import datetime
import os
os.chdir(r'D:\обучение\stepik 35')

class AppConfig:
    def __init__(self, config_file='config.txt', log_file='config_log.log'):
        self.settings = {}
        self.config_file = config_file
        self.log_file = log_file
        self._iter_keys = iter(self.settings)  # Для инициализации итератора

        # Загружаем конфигурации из файла при инициализации
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as f:
                for line in f:
                    if line.strip():
                        key, value = line.strip().split('=', 1)
                        self.settings[key.strip()] = value.strip()
                self._iter_keys = iter(self.settings)  # Обновляем итератор
        except FileNotFoundError:
            self.settings = {}  # Если файла нет, начинаем с пустого словаря

    def save_config(self):
        with open(self.config_file, 'w', encoding='utf-8') as f:
            for key, value in self.settings.items():
                f.write(f"{key}={value}\n")

    def log_change(self, action, key, old_value=None, new_value=None):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{timestamp} - {action.upper()}: '{key}'"
        if old_value is not None:
            log_entry += f" (старое значение: {old_value})"
        if new_value is not None:
            log_entry += f" (новое значение: {new_value})"
        log_entry += "\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

    def validate_key(self, key):
        if not isinstance(key, str):
            raise ValueError("Ключ конфигурации должен быть строкой")

    def validate_value(self, value):
        if value in ("", None) or (isinstance(value, (list, dict, set)) and len(value) == 0):
            raise ValueError("Значение конфигурации не может быть пустым")

    def __getitem__(self, key):
        self.validate_key(key)
        if key in self.settings:
            return self.settings[key]
        raise KeyError(f"Конфигурация с ключом '{key}' не найдена")

    def __setitem__(self, key, value):
        self.validate_key(key)
        self.validate_value(value)

        old_value = self.settings.get(key, None)  # Получаем старое значение, если оно есть
        self.settings[key] = value
        self.save_config()  # Сохраняем изменения в файл
        self.log_change('изменение', key, old_value, value)  # Логируем изменение
        self._iter_keys = iter(self.settings)  # Обновляем итератор

    def __delitem__(self, key):
        self.validate_key(key)

        if key in self.settings:
            old_value = self.settings[key]
            del self.settings[key]
            self.save_config()  # Сохраняем изменения в файл
            self.log_change('удаление', key, old_value)  # Логируем удаление
            self._iter_keys = iter(self.settings)  # Обновляем итератор
        else:
            raise KeyError(f"Конфигурация с ключом '{key}' не найдена")

    # Магические методы для итерации
    def __iter__(self):
        self._iter_keys = iter(self.settings)  # Инициализируем итератор по ключам словаря
        return self

    def __next__(self):
        return next(self._iter_keys)  # Возвращаем следующий ключ

# Пример использования:
config = AppConfig()

# Устанавливаем новые конфигурации
config["debug"] = "True"
config["database_url"] = "localhost:5432"

# Перебираем конфигурации
for key in config:
    print(f"{key} = {config[key]}")  # Выводим ключ и значение
