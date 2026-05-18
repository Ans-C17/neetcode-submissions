# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elem = 0
        count = 0
        def dfs(node):
            nonlocal elem, count
            
            if not node:
                return
            
            dfs(node.left)

            count += 1
            if count == k:
                elem = node.val

            dfs(node.right)
        
        dfs(root)
        return elem
