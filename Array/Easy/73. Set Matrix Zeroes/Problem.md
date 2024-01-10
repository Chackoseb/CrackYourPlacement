Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:

![mat1](https://github.com/Chackoseb/CrackYourPlacement/assets/95061303/4fa7d6ef-b3e7-4620-b58f-63ac3b4d90af)

<pre>
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
</pre>

Example 2:

![mat2](https://github.com/Chackoseb/CrackYourPlacement/assets/95061303/1e143ac2-12b1-4d35-ae32-522b0837a152)

<pre>
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
</pre>
 

Constraints:
<pre>
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1
</pre>
