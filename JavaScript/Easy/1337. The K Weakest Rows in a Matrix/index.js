var kWeakestRows = function (mat, k) {
  return mat
    .map((el, idx) => [idx, el.reduce((acc, cur) => acc + cur)])
    .sort((a, b) => Number(a[1]) - Number(b[1]))
    .slice(0, k)
    .map(arr => arr[0])
}

const mat = [
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 0],
  [1, 0, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [1, 1, 1, 1, 1],
]
const k = 3

console.log(kWeakestRows(mat, k)) // Output: [2, 0, 3]
