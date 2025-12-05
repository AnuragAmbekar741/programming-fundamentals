function twoCrystalBall(breaks: boolean[]): number {
  const jump = Math.floor(Math.sqrt(breaks.length));
  let i = jump;
  for (; i < breaks.length; i += jump) {
    if (breaks[i]) {
      break;
    }
  }
  i -= jump;
  for (let j = 0; j < jump; j++, i++) {
    if (breaks[i]) return i;
  }
  return -1;
}

console.log(
  twoCrystalBall([
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
  ])
);
