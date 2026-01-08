from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')


class DoublyListNode(Generic[T]):
    def __init__(
        self,
        value: T,
        next: Optional['DoublyListNode[T]'] = None,
        prev: Optional['DoublyListNode[T]'] = None
    ):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[DoublyListNode[T]] = None
        self.tail: Optional[DoublyListNode[T]] = None
        self.length: int = 0

    def prepend(self, value: T) -> None:
        node = DoublyListNode(value)

        if not self.head:
            self.head = self.tail = node
            self.length += 1
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        self.length += 1

    def append(self, value: T) -> None:
        node = DoublyListNode(value)

        if not self.head:
            self.head = self.tail = node
            self.length += 1
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1

    def remove_head(self) -> Optional[DoublyListNode[T]]:
        if not self.head:
            return None

        removed = self.head

        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
            return removed

        self.head = removed.next
        self.head.prev = None
        self.length -= 1

        removed.next = None
        removed.prev = None
        return removed

    def remove_tail(self) -> Optional[DoublyListNode[T]]:
        if not self.tail:
            return None

        removed = self.tail

        if self.length == 1:
            self.head = self.tail = None
            self.length = 0
            return removed

        self.tail = removed.prev
        self.tail.next = None
        self.length -= 1

        removed.prev = None
        removed.next = None
        return removed
