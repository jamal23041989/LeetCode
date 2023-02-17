## en

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list
that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer
is connected to (0-indexed). It is -1 if there is no cycle.
Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

---

## ru

Учитывая заголовок связанного списка, вернуть узел, с которого начинается цикл. Если цикла нет, вернуть null.

В связном списке есть цикл, если в списке есть какой-то узел
до которого можно снова добраться, непрерывно следуя за следующим указателем.
Внутри pos используется для обозначения индекса узла, следующего за хвостовым указателем.
подключен к (0-индексированный). Это -1, если нет цикла.
Обратите внимание, что pos не передается в качестве параметра.

Не изменяйте связанный список.

Пример 1:
Ввод: голова = [3,2,0,-4], позиция = 1
Выход: хвост соединяется с индексом узла 1
Объяснение: В связанном списке есть цикл, где хвост соединяется со вторым узлом.

Пример 2:
Ввод: голова = [1,2], позиция = 0
Выход: хвост соединяется с индексом узла 0
Объяснение: В связанном списке есть цикл, где хвост соединяется с первым узлом.

Пример 3:
Ввод: голова = [1], позиция = -1
Выход: нет цикла
Объяснение: В связанном списке нет цикла.

Ограничения:
Количество узлов в списке находится в диапазоне [0, 104].
-105 <= Node.val <= 105
pos равно -1 или допустимому индексу в связанном списке.

Дополнение: можете ли вы решить это, используя O (1) (т.е. постоянную) память?