# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []

        q = deque([root])
        while q:
            currLen = len(q)
            currList = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    currList.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if currList:
                res.append(currList)
        return res
