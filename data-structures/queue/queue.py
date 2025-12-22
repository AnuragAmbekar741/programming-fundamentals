from typing import Optional, TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next = None

class Queue(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.length = 0

    def enqueue(self, item: T)->None:
        node = Node(item)
        self.length+=1
        if not self.tail:
            self.tail = self.head = node
            return
        self.tail.next = node
        self.tail = node

    def dequeue(self)->Optional[T]:
        if not self.head:
            return None
        self.length-=1
        head = self.head
        self.head = self.head.next
        return head.value
    
    def peek(self)->Optional[T]:
        return self.head.value if self.head else None



# type Node<T> = {
#   value: T;
#   next?: Node<T> | null;
# };

# export default class Queue<T> {
#   public length: number;
#   private head?: Node<T>;
#   private tail?: Node<T>;
#   constructor() {
#     this.head = this.tail = undefined;
#     this.length = 0;
#   }

#   enqueue(item: T): void {
#     const node = { value: item } as Node<T>;
#     this.length++;
#     if (!this?.tail) {
#       this.tail = this.head = node;
#       return;
#     }
#     this.tail.next = node;
#     this.tail = node;
#   }

#   dequeue(): T | undefined {
#     if (!this.head) {
#       return undefined;
#     }
#     this.length--;
#     const head = this.head;
#     this.head = this.head.next ?? undefined;
#     return head.value;
#   }
#   peek(): T | undefined {
#     return this.head?.value;
#   }
# }
