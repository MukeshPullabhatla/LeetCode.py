'''
96. Unique Binary Search Tree
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
Example 1:
Input: n = 3
Output: 5
Example 2:
Input: n = 1
Output: 1
Constraints:
1 <= n <= 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        def fact(n):
            if n==1:
                return 1
            return n*fact(n-1)
        return fact(2*n)//(fact(n+1)*fact(n))