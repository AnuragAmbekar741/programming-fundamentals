from __future__ import annotations
from typing import Optional, TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, value: T, next: Optional["Node[T]"] = None):
        self.value: T = value
        self.next: Optional["Node[T]"] = next

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.head: Optional[Node[T]] = None
        self.length: int = 0

    def push(self, item: T) -> None:
        self.head = Node(item, self.head)
        self.length += 1

    def pop(self) -> Optional[T]:
        if self.head is None:
            return None

        removed = self.head
        self.head = removed.next
        self.length -= 1
        return removed.value

    def peek(self) -> Optional[T]:
        return self.head.value if self.head else None

