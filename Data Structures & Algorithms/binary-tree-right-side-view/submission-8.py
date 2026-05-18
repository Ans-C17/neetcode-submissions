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
            right_node = None
            curr_len = len(queue)

            for i in range(curr_len):
                node = queue.popleft()
                if node:
                    right_node = node #take the rightmost node each time
                    queue.append(node.left)
                    queue.append(node.right)
                
            if right_node:
                result.append(right_node.val)

        return result
