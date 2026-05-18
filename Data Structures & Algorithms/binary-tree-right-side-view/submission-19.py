# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            rightSideNode = None
            currLen = len(queue)
            for i in range(currLen):
                node = queue.popleft()
                if node:
                    rightSideNode = node
                    queue.append(node.left)
                    queue.append(node.right)
            
            if rightSideNode:
                result.append(rightSideNode.val)
        
        return result


