'''
95. Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:
Input: n = 1
Output: [[1]]
Constraints:
1 <= n <= 8
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.bst(1, n+1)
    def bst(self, start, end):
        if start == end: return None
        res = []
        for root in range(start, end):
            for left in self.bst(start, root) or [None]:
                for right in self.bst(root+1, end) or [None]:
                    node = TreeNode(root)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res