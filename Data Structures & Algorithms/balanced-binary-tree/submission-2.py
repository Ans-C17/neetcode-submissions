# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        maxDiff = 0
        def dfs(root):
            nonlocal maxDiff

            if not root:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
            
            maxDiff = max(maxDiff, abs(leftHeight - rightHeight))
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return True if maxDiff <= 1 else False
        