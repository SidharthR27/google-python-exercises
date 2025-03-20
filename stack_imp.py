class Stack:
    def __init__(self,items):
        if items:
            self.items = items
        else:
            self.items = []
    
    def pop(self):
        if self.items:
            element = self.items[-1]
            self.items = self.items[:-1]
            return element
        else:
            return None
    
    def push(self, element):
        self.items.append(element)
        return self.items
    
    def __repr__(self):
        return str(self.items)

a = Stack([])
# print(a.pop())
print(a)
print(a.pop())
print(a)
    

        

