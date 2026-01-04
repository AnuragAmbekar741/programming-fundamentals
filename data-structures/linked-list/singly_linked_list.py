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
            self.head = self.tail = node
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

        if self.length == 0:
            self.head = self.tail = None
        
        removed.next = None
        return removed
    
    def remove_tail(self) -> Optional[ListNode[T]]:
        if self.head is None:
            return None

        # one node
        if self.length == 1:
            removed = self.head
            self.head = self.tail = None
            self.length = 0
            return removed

        cur = self.head
        assert self.tail is not None

        while cur.next is not self.tail:
            cur = cur.next  # type: ignore[assignment]

        removed = self.tail
        cur.next = None
        self.tail = cur
        self.length -= 1

        removed.next = None
        return removed
    
    def reverse(self):
        if self.head is None:
            return None
        cur = self.head
        prev = None
        self.tail = self.head
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


ll = SinglyLinkedList[int]()
ll.append(10)
ll.append(20)
ll.prepend(5)
print(ll.list_to_arr())  # [5, 10, 20]

ll.remove_tail()
print(ll.list_to_arr())  # [5, 10]

ll.reverse()
print(ll.list_to_arr())  # [10, 5]
print(ll.length)  

