## en

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

---

## ru

Римские цифры представлены семью различными символами: I, V, X, L, C, D и M.

Символ Значение
я 1
В 5
Х 10
л 50
С 100
Д 500
М 1000

Например, 2 записывается как II римскими цифрами, просто две сложенные вместе. 
12 записывается как XII, то есть просто X + II. Число 27 записывается как XXVII, то есть XX + V + II.

Римские цифры обычно пишутся слева направо от большего к меньшему. Однако цифра четыре не IIII.
Вместо этого цифра четыре пишется как IV. Так как единица предшествует пятерке, мы вычитаем ее и получаем четыре.

Тот же принцип применим к числу девять, которое пишется как IX. Есть шесть случаев, когда используется вычитание:
I можно поставить перед V (5) и X (10), чтобы получились 4 и 9.
X можно поставить перед L (50) и C (100), чтобы получилось 40 и 90.
C можно поставить перед D (500) и M (1000), чтобы получились 400 и 900.

Дана римская цифра, преобразовать ее в целое число.


Пример 1:
Ввод: с = "III"
Выход: 3
Пояснение: III = 3.
Пример 2:

Ввод: с = "LVIII"
Выход: 58
Пояснение: L = 50, V = 5, III = 3.
Пример 3:

Ввод: с = "MCMXCIV"
Выход: 1994 г.
Пояснение: М = 1000, СМ = 900, ХС = 90 и IV = 4.
 

Ограничения:
1 <= s.length <= 15
s содержит только символы («I», «V», «X», «L», «C», «D», «M»).
Гарантируется, что s — допустимая римская цифра в диапазоне [1, 3999].