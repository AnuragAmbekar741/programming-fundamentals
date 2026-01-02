class ListNode<T> {
  value: T;
  next: ListNode<T> | null;

  constructor(value: T, next: ListNode<T> | null = null) {
    this.value = value;
    this.next = next;
  }
}

class SinglyLinkedList<T> {
  head: ListNode<T> | null = null;
  tail: ListNode<T> | null = null;
  length: number = 0;

  prepend(value: T): void {
    const node = new ListNode(value);
    if (!this.head) {
      this.head = this.tail = node;
      this.length++;
      return;
    }
    this.length++;
    node.next = this.head;
    this.head = node;
  }

  append(value: T): void {
    const node = new ListNode(value);
    if (!this.head) {
      this.head = this.tail = node;
      this.length++;
      return;
    }
    this.length++;
    this.tail!.next = node;
    this.tail = node;
  }

  deleteHead(): T | null {
    if (!this.head) return null;
    const removedNode = this.head;
    this.head = this.head.next;
    this.length--;
    if (this.length === 0) {
      this.head = this.tail = null;
    }
    removedNode.next = null;
    return removedNode.value;
  }

  get(index: number): ListNode<T> | null {
    if (index < 0 || index >= this.length) return null;
    let curr = this.head;
    while (index > 0) {
      curr = curr!.next;
      index--;
    }
    return curr;
  }

  toArray(): T[] {
    const result: T[] = [];
    let cur = this.head;
    while (cur !== null) {
      result.push(cur.value);
      cur = cur.next;
    }
    return result;
  }
}

const list = new SinglyLinkedList<number>();
list.prepend(40);
list.append(50);
list.append(60);
list.append(70);
list.append(80);
list.append(90);
console.log(list.get(1));
// console.log(list.toArray());
// console.log(list);
