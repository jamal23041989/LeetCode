const account = [
  [1, 5],
  [7, 3],
  [3, 5],
]

var maximumWealth = function (accounts) {
  let num = 0
  accounts.forEach(arr => {
    num = num > arr.reduce((acc, item) => acc + item, 0) ? num : arr.reduce((acc, item) => acc + item, 0)
  })
  return num
}

console.log(maximumWealth(account))
