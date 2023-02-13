## en

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

---

## ru

Вам дан массив цен, где цены[i] — цена данной акции на i-й день.

Вы хотите максимизировать свою прибыль, выбрав один день для покупки одной акции и выбрав
другой день в будущем, чтобы продать эти акции.

Верните максимальную прибыль, которую вы можете получить от этой сделки.
Если вы не можете получить никакой прибыли, верните 0.

Пример 1:
Вход: цены = [7,1,5,3,6,4]
Выход: 5
Объяснение: покупка во 2-й день (цена = 1) и продажа в 5-й день (цена = 6), прибыль = 6-1 = 5.
Обратите внимание, что покупка во 2-й день и продажа в 1-й день не разрешены, потому что вы должны купить перед продажей.

Пример 2:
Вход: цены = [7,6,4,3,1]
Выход: 0
Объяснение: в этом случае транзакции не выполняются, а максимальная прибыль = 0.