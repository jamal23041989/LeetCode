## en

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

---

## ru

Учитывая заголовок, заголовок связанного списка, определите, есть ли в связанном списке цикл.

В связанном списке есть цикл, если в списке есть какой-то узел, к которому можно снова обратиться
непрерывно следуя следующему указателю.
Внутри pos используется для обозначения индекса узла, к которому подключен следующий указатель tail.
Обратите внимание, что pos не передается в качестве параметра.

Возвращает true, если в связанном списке есть цикл. В противном случае вернуть ложь.

Пример 1:
Ввод: голова = [3,2,0,-4], позиция = 1
Вывод: правда
Объяснение: В связанном списке есть цикл, хвост которого соединяется с 1-м узлом (с индексом 0).

Пример 2:
Ввод: голова = [1,2], позиция = 0
Вывод: правда
Объяснение: В связанном списке есть цикл, хвост которого соединяется с 0-м узлом.

Пример 3:
Ввод: голова = [1], позиция = -1
Вывод: ложь
Объяснение: В связанном списке нет цикла.

Ограничения:
Количество узлов в списке находится в диапазоне [0, 104].
-105 <= Node.val <= 105
pos равно -1 или допустимому индексу в связанном списке.