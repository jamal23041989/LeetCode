## en

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

---

## ru

Учитывая массив целых чисел nums и целочисленную цель, вернуть индексы двух чисел так,
чтобы они складывались в цель.
Вы можете предположить, что каждый вход будет иметь ровно одно решение,
и вы не можете использовать один и тот же элемент дважды.
Вы можете вернуть ответ в любом порядке.


Пример 1:

Ввод: числа = [2,7,11,15], цель = 9
Выход: [0,1]
Объяснение: поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].
Пример 2:

Ввод: числа = [3,2,4], цель = 6
Выход: [1,2]
Пример 3:

Ввод: числа = [3,3], цель = 6
Выход: [0,1]

Ограничения:
2 <= nums.length <= 104
-109 <= число[i] <= 109
-109 <= цель <= 109
Существует только один правильный ответ.

Дополнение: можете ли вы придумать алгоритм, временная сложность которого меньше O(n2)?