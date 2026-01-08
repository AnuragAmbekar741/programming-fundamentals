type QNode<T> = {
  value: T;
  next?: QNode<T>;
};

export default class Queue<T> {
  public length: number;
  private head?: QNode<T>;
  private tail?: QNode<T>;

  constructor() {
    this.head = this.tail = undefined;
    this.length = 0;
  }

  enqueue(item: T): void {
    const node: QNode<T> = { value: item };

    if (!this.tail) {
      this.head = this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }

    this.length++;
  }

  dequeue(): T | undefined {
    if (!this.head) return undefined;

    const removed = this.head;
    this.head = removed.next;
    this.length--;

    if (this.length === 0) {
      this.tail = undefined;
    }

    removed.next = undefined;
    return removed.value;
  }

  peek(): T | undefined {
    return this.head?.value;
  }
}
