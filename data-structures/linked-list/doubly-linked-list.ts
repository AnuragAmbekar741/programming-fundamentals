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
  length: number = 0;

  prepend(value: T) {
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

  append(value: T) {
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

    const remove = this.head;

    if (this.length === 1) {
      this.length = 0;
      this.head = this.tail = null;
      return remove;
    }

    this.head = remove.next;
    this.head!.prev = null;
    this.length--;

    remove.next = null;
    return remove;
  }

  removeTail(): DoublyListNode<T> | null {
    if (!this.head) return null;

    const remove = this.tail;

    if (this.length === 1) {
      this.length = 0;
      this.head = this.tail = null;
      return remove;
    }

    this.tail = remove!.prev;
    this.tail!.next = null;
    this.length--;

    remove!.prev = null;
    return remove;
  }

  toArray() {}
  reverse() {}
}
