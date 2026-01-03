class ListNode<T> {
  value: T;
  next: ListNode<T> | null;

  constructor(value: T, next: ListNode<T> | null = null) {
    this.value = value;
    this.next = next;
  }
}

class SignlyLinkedList<T> {
  head: ListNode<T> | null = null;
  tail: ListNode<T> | null = null;
  length: number = 0;

  prepend(value: T): void {
    const node = new ListNode(value);
    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.length++;
  }

  append(value: T): void {
    const node = new ListNode(value);
    if (!this.head) {
      this.prepend(value);
      return;
    } else {
      this.tail!.next = node;
      this.tail = node;
    }
    this.length++;
  }

  removeHead(): ListNode<T> | null {
    if (!this.head) return null;
    const removed = this.head;
    this.head = removed.next;
    this.length--;
    if (this.length === 0) {
      this.head = this.tail = null;
    }
    removed.next = null;
    return removed;
  }

  removeTail(): ListNode<T> | null {
    if (!this.head) return null;
    if (this.length === 1) {
      const removed = this.head;
      this.head = this.tail = null;
      this.length = 0;
      return removed;
    }

    let curr = this.head;
    while (curr.next !== this.tail) {
      curr = curr.next!;
    }
    const removed = this.tail;
    curr.next = null;
    this.tail = curr;
    this.length--;
    return removed;
  }

  get(index: number): ListNode<T> | null {
    if (index < 0 || index >= this.length) return null;
    if (index == 0) return this.head;
    if (index === this.length - 1) return this.tail;
    let curr = this.head;
    while (index > 0) {
      curr = curr!.next;
      index--;
    }
    return curr;
  }

  removeAt(index: number): ListNode<T> | null {
    if (index < 0 || index >= this.length) return null;
    if (index === 0) return this.removeHead();
    if (index === this.length - 1) return this.removeTail();
    const prevNode = this.get(index - 1);
    if (!prevNode) return null;
    const removeNode = prevNode.next;
    if (!removeNode) return null;
    prevNode.next = removeNode?.next;
    this.length--;
    return removeNode;
  }

  insertAt(index: number, value: T): void {
    if (index < 0 || index > this.length) return;
    if (index === 0) return this.prepend(value);
    if (index === this.length - 1) return this.append(value);
    const node = new ListNode(value);
    const prevNode = this.get(index - 1);
    if (!prevNode) return;
    const currNode = prevNode.next;
    prevNode.next = node;
    node.next = currNode;
    this.length++;
  }

  listToArray(): T[] {
    const result: T[] = [];
    let curr = this.head;
    while (curr !== null) {
      result.push(curr!.value);
      curr = curr!.next;
    }
    return result;
  }

  reverse(): void {
    if (!this.head || this.length === 1) return;
    let prev: ListNode<T> | null = null;
    let cur: ListNode<T> | null = this.head;
    this.tail = this.head;
    while (cur !== null) {
      const next: ListNode<T> | null = cur.next;
      cur.next = prev;
      prev = cur;
      cur = next;
    }
    this.head = prev;
  }
}

const list = new SignlyLinkedList();
list.append(10);
list.prepend(20);
list.prepend(30);
list.prepend(40);
list.prepend(50);
list.prepend(60);
list.insertAt(5, 75);
console.log(list.removeAt(3));
console.log(list.length);
