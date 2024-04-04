from .FileHandler import JsonHandler

class DataLoader:
    handlers = {
        'json': JsonHandler
    }

    def __init__(self, path, file_type):
        self.handler = self.handlers[file_type](path)
        self.idx = 0
        self.length = len(self.handler)

    def get(self, idx=None):
        if idx is not None:
            self.idx = idx
        return self.handler.get(self.idx)
    
    def getNext(self):
        if self.idx < self.length - 1:
            self.idx += 1
            return self.get(self.idx)
        return None

    def getPrev(self):
        if self.idx > 0:
            self.idx -= 1
            return self.get(self.idx)
        return None

    def save(self):
        self.handler.save()