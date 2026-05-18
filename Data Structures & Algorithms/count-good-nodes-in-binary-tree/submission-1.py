# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            if not node:
                return 0

            if node.val >= maximum:
                total = 1
            else:
                total = 0
            
            total += dfs(node.left, max(node.val, maximum))
            total += dfs(node.right, max(node.val, maximum))

            return total
        
        return dfs(root, root.val)


        
        
