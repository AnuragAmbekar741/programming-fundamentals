class DoublyListNode<T> {
  value: T;
  next: DoublyListNode<T> | null;
  prev: DoublyListNode<T> | null;

  constructor(
    value: T,
    next: DoublyListNode<T> | null = null,
    prev: DoublyListNode<T> | null = null
  ) {
    this.value = value;
    this.next = next;
    this.prev = prev;
  }
}
class DoublyLinkedList<T> {
  head: DoublyListNode<T> | null = null;
  tail: DoublyListNode<T> | null = null;
  length = 0;

  prepend(value: T): void {
    const node = new DoublyListNode(value);

    if (!this.head) {
      this.head = this.tail = node;
      this.length++;
      return;
    }

    node.next = this.head;
    this.head.prev = node;
    this.head = node;
    this.length++;
  }

  append(value: T): void {
    const node = new DoublyListNode(value);

    if (!this.head) {
      this.head = this.tail = node;
      this.length++;
      return;
    }

    this.tail!.next = node;
    node.prev = this.tail;
    this.tail = node;
    this.length++;
  }

  removeHead(): DoublyListNode<T> | null {
    if (!this.head) return null;

    const removed = this.head;

    if (this.length === 1) {
      this.head = this.tail = null;
      this.length = 0;
      return removed;
    }

    this.head = removed.next;
    this.head!.prev = null;
    this.length--;

    removed.next = null;
    removed.prev = null;
    return removed;
  }

  removeTail(): DoublyListNode<T> | null {
    if (!this.tail) return null;

    const removed = this.tail;

    if (this.length === 1) {
      this.head = this.tail = null;
      this.length = 0;
      return removed;
    }

    this.tail = removed.prev;
    this.tail!.next = null;
    this.length--;

    removed.prev = null;
    removed.next = null;
    return removed;
  }

  get(index: number): DoublyListNode<T> | null {
    if (index < 0 || index >= this.length) return null;

    // Optional optimization (DLL advantage):
    // if (index < this.length / 2) go from head else from tail
    let curr: DoublyListNode<T> | null;
    if (index < this.length / 2) {
      curr = this.head;
      while (index > 0) {
        curr = curr!.next;
        index--;
      }
      return curr;
    } else {
      curr = this.tail;
      let i = this.length - 1;
      while (i > index) {
        curr = curr!.prev;
        i--;
      }
      return curr;
    }
  }

  removeAt(index: number): DoublyListNode<T> | null {
    if (index < 0 || index >= this.length) return null;

    if (index === 0) return this.removeHead();
    if (index === this.length - 1) return this.removeTail();

    const node = this.get(index);
    if (!node) return null;

    const prev = node.prev!;
    const next = node.next!;

    prev.next = next;
    next.prev = prev;

    this.length--;

    node.prev = null;
    node.next = null;
    return node;
  }

  toArray(): T[] {
    const result: T[] = [];
    let curr = this.head;
    while (curr !== null) {
      result.push(curr.value);
      curr = curr.next;
    }
    return result;
  }

  reverse(): void {
    if (!this.head || this.length === 1) return;

    const oldHead = this.head;
    const oldTail = this.tail!;

    let cur: DoublyListNode<T> | null = this.head;
    while (cur !== null) {
      const next = cur.next;
      cur.next = cur.prev;
      cur.prev = next;
      cur = next;
    }

    this.head = oldTail;
    this.tail = oldHead;
  }
}
