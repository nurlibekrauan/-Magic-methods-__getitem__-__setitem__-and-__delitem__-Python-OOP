class MultiDict:
    def __init__(self) -> None:
        self.data = {}

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        raise KeyError("No such key")

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]
        else:
            raise KeyError("No such key")


multi_dict = MultiDict()
multi_dict["key1"] = "value1"
multi_dict["key1"] = "value2"
multi_dict["key2"] = "value3"

print(multi_dict["key1"])  # Вывод: ["value1", "value2"]
print(multi_dict["key2"])  # Вывод: ["value3"]

del multi_dict["key1"]
try:
    print(multi_dict["key1"])  # Должен выбросить KeyError
except KeyError:
    print("KeyError")
