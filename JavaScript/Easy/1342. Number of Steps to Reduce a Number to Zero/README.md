## en

Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example 1:

Input: num = 14
Output: 6
Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.
Example 2:

Input: num = 8
Output: 4
Explanation:
Step 1) 8 is even; divide by 2 and obtain 4.
Step 2) 4 is even; divide by 2 and obtain 2.
Step 3) 2 is even; divide by 2 and obtain 1.
Step 4) 1 is odd; subtract 1 and obtain 0.
Example 3:

Input: num = 123
Output: 12

Constraints:

0 <= num <= 106

---

## ru

Учитывая целое число, вернуть количество шагов, чтобы уменьшить его до нуля.

За один шаг, если текущее число четное, вы должны разделить его на 2, в противном случае вы должны вычесть из него 1.

Пример 1:

Ввод: число = 14
Выход: 6
Объяснение:
Шаг 1) 14 четно; делим на 2 и получаем 7.
Шаг 2) 7 нечетное; вычесть 1 и получить 6.
Шаг 3) 6 четно; делим на 2 и получаем 3.
Шаг 4) 3 нечетно; вычесть 1 и получить 2.
Шаг 5) 2 четно; делим на 2 и получаем 1.
Шаг 6) 1 нечетное; вычесть 1 и получить 0.
Пример 2:

Ввод: число = 8
Выход: 4
Объяснение:
Шаг 1) 8 четно; делим на 2 и получаем 4.
Шаг 2) 4 четно; делим на 2 и получаем 2.
Шаг 3) 2 четно; делим на 2 и получаем 1.
Шаг 4) 1 нечетное; вычесть 1 и получить 0.
Пример 3:

Ввод: число = 123
Выход: 12

Ограничения:

0 <= число <= 106
