class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def insertAtEnd(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
    
    def deleteFromBeginning(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def deleteFromEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    
    def search(self,value):
        if self.head is None:
            return 
        temp = self.head
        position = 0
        while temp:
            if temp.value == value:
                return f'{value} found at {position} index'
            temp = temp.next
            position+=1
        return f'{value} not found in the Linked List'


# l = LinkedList()
# l.insertAtBeginning(5)
# l.insertAtBeginning(4)
# l.insertAtBeginning(3)
# l.insertAtBeginning(2)
# l.insertAtEnd(6)
# l.printList()
# print(l.search(6))
# l.deleteFromBeginning()
# l.deleteFromEnd()
# l.printList()
# print(l.search(6))
    
        