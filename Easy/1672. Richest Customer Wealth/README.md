## en

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 6
2nd customer has wealth = 10
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.
Example 3:

Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

Constraints:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100

---

## ru

Вам дана m x nцелочисленная сетка , accountsгде accounts[i][j]сумма денег у клиента в банке. Верните богатство , которое есть у самого богатого покупателя.i​​​​​​​​​​​th​​​​j​​​​​​​​​​​th

Богатство клиента — это сумма денег, которую он имеет на всех своих банковских счетах. Самый богатый клиент — это клиент, который имеет максимальное богатство .

Пример 1:

Ввод: account = [[1,2,3],[3,2,1]]
Вывод: 6
Объяснение :
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Оба клиента считаются самыми богатыми с состоянием 6 каждый, поэтому верните 6.
Пример 2:

Ввод: счета = [[1,5],[7,3],[3,5]]
Вывод: 10
Объяснение :
1-й клиент имеет богатство = 6
2-й клиент имеет богатство = 10
3-й клиент имеет богатство = 8
2-й клиент самый богатый с богатством 10.
Пример 3:

Ввод: счета = [[2,8,7],[7,1,3],[1,9,5]]
Вывод: 17

Ограничения:

m == accounts.length
n == accounts[i].length
1 <= m, n <= 50
1 <= accounts[i][j] <= 100
