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
            rightMostNode = None
            currLenOfQueue = len(queue)

            for i in range(currLenOfQueue):
                node = queue.popleft()
                if node:
                    rightMostNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightMostNode:
                result.append(rightMostNode.val)
        
        return result


