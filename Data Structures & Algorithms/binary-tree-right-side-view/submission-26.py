# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        q = deque([root])

        while q:
            currLen = len(q)
            rightMostNode = None
            for _ in range(currLen):
                node = q.popleft()
                rightMostNode = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
            if rightMostNode:
                res.append(rightMostNode.val)

        return res
