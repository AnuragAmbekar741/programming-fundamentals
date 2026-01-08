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

    def get(self, index: int) -> Optional[DoublyListNode[T]]:
        if index < 0 or index >= self.length:
            return None

        # Optimization (DLL advantage):
        # if index < length / 2 go from head else from tail
        if index < self.length // 2:
            curr = self.head
            while index > 0:
                curr = curr.next
                index -= 1
            return curr
        else:
            curr = self.tail
            i = self.length - 1
            while i > index:
                curr = curr.prev
                i -= 1
            return curr

    def remove_at(self, index: int) -> Optional[DoublyListNode[T]]:
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.remove_head()
        if index == self.length - 1:
            return self.remove_tail()

        node = self.get(index)
        if not node:
            return None

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.length -= 1

        node.prev = None
        node.next = None
        return node

    def to_array(self) -> List[T]:
        result: List[T] = []
        curr = self.head
        while curr is not None:
            result.append(curr.value)
            curr = curr.next
        return result

    def reverse(self) -> None:
        if not self.head or self.length == 1:
            return

        old_head = self.head
        old_tail = self.tail

        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = curr.prev
            curr.prev = next_node
            curr = next_node

        self.head = old_tail
        self.tail = old_head