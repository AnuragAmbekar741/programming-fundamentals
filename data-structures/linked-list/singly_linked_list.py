from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, List

T = TypeVar("T")

@dataclass
class ListNode(Generic[T]):
    value:T
    next:Optional["ListNode[T]"] = None


class SinglyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[ListNode[T]] = None
        self.tail: Optional[ListNode[T]] = None
        self.length: int = 0
    
    def prepend(self,value):
        node = ListNode(value)

        if self.head is None:
            self.head = self.tail = None
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def append(self,value):
        node = ListNode(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length+=1
    
    def get(self,index:int):
        if index < 0 or index >= self.length:
            return None
        cur = self.head
        while(index>0):
            cur = cur.next
            index-=1
        return cur
    
    def list_to_arr(self)->List[T]:
        result:List[T] = []
        cur = self.head
        while cur is not None:
            result.append(cur.value)
            cur = cur.next
        
        return result
    
    def remove_head(self):
        if self.head is None:
            return None
        
        removed = self.head
        self.head = removed.next
        self.length -= 1

        if self.length is 0:
            self.head = self.tail = None
        
        removed.next = None
        return removed
    
    def remove_tail(self):
        if self.head is None:
            return None
        cur = self.head
        while cur.next is None:
            cur = cur.next
        cur.next = None
        self.tail = cur

