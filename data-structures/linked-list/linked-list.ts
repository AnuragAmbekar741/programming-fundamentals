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
console.log(list.toArray());
console.log(list);
