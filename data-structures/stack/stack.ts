type SNode<T> = {
  value: T;
  next?: SNode<T>;
};

class Stack<T> {
  public length: number;
  private head?: SNode<T>;
  constructor() {
    this.head = undefined;
    this.length = 0;
  }

  push(item: T): void {
    const node: SNode<T> = { value: item };
    if (!this.head) {
      this.head = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.length++;
  }

  pop(): T | undefined {
    if (!this.head) return undefined;
    else {
      const removed = this.head;
      if (this.length === 1) {
        this.head = undefined;
        this.length--;
        return removed.value;
      }
      this.head = removed.next;
      this.length--;
      return removed.value;
    }
  }

  peek(): T | undefined {
    return this.head?.value;
  }
}
