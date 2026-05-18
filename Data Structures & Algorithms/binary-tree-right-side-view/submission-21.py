# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque([root])

        while q:
            rightSideNode = None
            currLen = len(q)

            for i in range(currLen):
                node = q.popleft()
                if node:
                    rightSideNode = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightSideNode:
                result.append(rightSideNode.val)
        
        return result