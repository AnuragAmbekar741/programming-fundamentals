function linearSearch(hayStack: number[], needle: number) {
  for (let i = 0; i <= hayStack.length; i++) {
    if (hayStack[i] === needle) return true;
  }
  return false;
}
//indexOf is based on linear search
