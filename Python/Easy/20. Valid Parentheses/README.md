## en

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

---

## ru

Учитывая строку s, содержащую только символы '(', ')', '{', '}', '[' и ']', определите, допустима ли входная строка.

Входная строка действительна, если:
Открытые скобки должны быть закрыты однотипными скобками.
Открытые скобки должны быть закрыты в правильном порядке.
Каждой закрывающей скобке соответствует открытая скобка того же типа.

Пример 1:
Ввод: с = "()"
Вывод: правда

Пример 2:
Ввод: с = "()[]{}"
Вывод: правда

Пример 3:
Ввод: с = "(]"
Вывод: ложь

Ограничения:
1 <= s.length <= 104
s состоит только из круглых скобок '()[]{}'.