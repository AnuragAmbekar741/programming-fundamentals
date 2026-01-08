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
    const node = { value: item } as QNode<T>;
    if (!this.tail) this.head = this.tail = node;
    this.length += 1;
    this.tail.next = node;
    this.tail = node;
  }

  dequeue(): T | undefined {
    if (!this.head) return undefined;
    else {
      const remove = this.head;
      this.head = remove.next;
      this.length--;
      remove.next = undefined;
      return remove.value;
    }
  }

  peek(): T | undefined {
    return this.head?.value;
  }
}
