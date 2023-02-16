## en

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 104

---

## ru

Учитывая целое число n, вернуть ответ в виде массива строк (с индексом 1), где:

answer[i] == "FizzBuzz", если i делится на 3 и 5.
answer[i] == "Шипение", если i делится на 3.
answer[i] == "Buzz", если i делится на 5.
answer[i] == i (в виде строки), если ни одно из приведенных выше условий не выполняется.

Пример 1:
Вход: n = 3
Вывод: ["1","2","шипение"]

Пример 2:
Вход: n = 5
Вывод: ["1","2","шипение","4","жужжание"]

Пример 3:
Вход: n = 15
Вывод: ["1","2","Шипение","4","Базз","Шипение","7","8","Шипение","Базз","11","Шипение" ,"13","14","FizzBuzz"]

Ограничения:
1 <= п <= 104