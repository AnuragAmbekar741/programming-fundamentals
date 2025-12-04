function binarySearch(hayStack: number[], needle: number) {
  let low = 0;
  let high = hayStack.length;

  do {
    const mid = Math.floor(low + (high - low) / 2);
    const value = hayStack[mid];
    console.log("mid", mid, "value", value, "low", low, "high", high);
    if (value === needle) return true;
    else if (value > needle) high = mid;
    else low = mid + 1;
  } while (low < high);
  return false;
}
console.log(binarySearch([10, 12, 15, 16, 19, 21, 24, 25, 34], 12));
