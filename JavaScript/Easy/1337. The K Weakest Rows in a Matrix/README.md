## en

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:

- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
  The rows ordered from weakest to strongest are [2,0,3,1,4].
  Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:

- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
  The rows ordered from weakest to strongest are [0,2,3,1].

Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

---

## ru

Вам дан мат бинарной матрицы размера m x n, состоящий из единиц (представляющих солдат) и нулей (представляющих гражданских лиц). Солдаты стоят перед мирными жителями. То есть все 1 будут отображаться слева от всех 0 в каждой строке.

Строка i слабее строки j, если верно одно из следующих условий:

Количество солдат в i-м ряду меньше, чем количество солдат в j-м ряду.
В обоих рядах одинаковое количество солдат и i < j.
Возвращает индексы k самых слабых строк в матрице в порядке от самого слабого к самому сильному.

Пример 1:

Вход: мат =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
к = 3
Выход: [2,0,3]
Объяснение:
Количество солдат в каждом ряду:

- Ряд 0:2
- Ряд 1: 4
- Ряд 2: 1
- Ряд 3: 2
- Ряд 4: 5
  Строки, упорядоченные от самого слабого к самому сильному: [2,0,3,1,4].

Пример 2:

Вход: мат =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
к = 2
Выход: [0,2]
Объяснение:
Количество солдат в каждом ряду:

- Ряд 0:1
- Ряд 1: 4
- Ряд 2: 1
- Ряд 3: 1
  Строки, упорядоченные от самого слабого к самому сильному: [0,2,3,1].

Ограничения:

м == мат.длина
n == мат[i].длина
2 <= п, м <= 100
1 <= к <= м
matrix[i][j] равно 0 или 1.
