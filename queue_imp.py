class Queue:
    def __init__(self, items):
        if items:
            self.items = items[:]
        else:
            self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop(0)
        else: return None
    
    def size(self):
        return len(self.items)