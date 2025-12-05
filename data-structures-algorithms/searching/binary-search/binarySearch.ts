function binarySearch(hayStack: number[], needle: number): boolean {
  let low = 0;
  let high = hayStack.length;
  for (let i = 0; i < hayStack.length; i++) {
    if (low > high) break;
    const mid = Math.floor(low + (high - low) / 2);
    const value = hayStack[mid];
    if (value === needle) return true;
    else if (value > needle) high = mid;
    else low = mid + 1;
  }
  return false;
}

console.log(binarySearch([2, 5, 7, 8, 9, 10, 14, 18, 19], 3));
