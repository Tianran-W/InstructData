import json

class JsonHandler:
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r', encoding="utf-8") as file:
            self.data = json.load(file)
            if not self.data:
                raise ValueError("No data in file")
        self.length = len(self.data)

    def __len__(self):
        return self.length

    def get(self, idx):
        if idx is None:
            raise ValueError("Index not provided")
        if idx < self.length and idx >= 0:
            return self.data[idx]
        raise ValueError("Index out of range")

    def save(self):
        with open(self.path, 'w', encoding="utf-8") as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)