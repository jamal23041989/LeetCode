var numberOfSteps = function (num) {
  let newNum = num
  let count = 0

  while (newNum > 0) {
    newNum % 2 === 0 ? (newNum = newNum / 2) : (newNum = newNum - 1)
    count = count + 1
  }

  return count
}

console.log(numberOfSteps(14)) //6
