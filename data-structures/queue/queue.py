from typing import Optional, TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self,value:T):
        self.value = value
        self.next = None

class Queue(Generic[T]):

    def __init__(self):
        self.head = Optional[None[T]] =  None
        self.tail = Optional[None[T]] =  None
        self.length = 0
    
    def enqueue(self,item:T)->None:
        node = Node(item)
        if not self.tail:
            self.tail = self.head = node
        self.length+=1
        self.tail.next = node
        self.tail = node
    
    def dequeue(self)->Optional[T]:
        if not self.head:
            return None
        self.length -= 1
        head = self.head
        self.head = self.head.next
        return head.value

    def peek(self)->Optional[T]:
        return self.head.value if self.head else None