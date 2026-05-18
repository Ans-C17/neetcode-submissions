# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if not node:
                return 0

            if node.val >= maxval:
                maxval = node.val
                return 1 + dfs(node.left, maxval) + dfs(node.right, maxval)
            else:
                return dfs(node.left, maxval) + dfs(node.right, maxval)
        
        return dfs(root, -101)