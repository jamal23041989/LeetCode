## en

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ...,
sk where k >= 109, and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?

---

## ru

Имея две строки s и t, вернуть true, если s является подпоследовательностью t, или false в противном случае.

Подпоследовательность строки — это новая строка,
образованная из исходной строки путем удаления некоторых (может быть ни одного) символов,
не нарушая взаимного расположения остальных символов.
(т. е. «туз» является подпоследовательностью «abcde», а «aec» — нет).

Пример 1:
Ввод: s = "abc", t = "ahbgdc"
Вывод: правда

Пример 2:
Ввод: s = "axc", t = "ahbgdc"
Вывод: ложь

Ограничения:
0 <= s.length <= 100
0 <= t.length <= 104
s и t состоят только из строчных английских букв.

Продолжение: предположим, что есть много входящих s, скажем, s1, s2, ...,
sk, где k >= 109, и вы хотите последовательно проверить, есть ли у t подпоследовательность.
В этом случае, как бы вы изменили свой код?