# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(s, t):
            if not s and not t: # if they are both empty, they are the same tree
                return True
            
            if s and t and s.val == t.val:
                # those two nodes are the same but we have to compare the rest of the trees
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)

            # now one tree empty and other non-empty case
            return False
        
        if not subRoot:
            return True # null tree is subtree of any tree
        
        if not root:
            return False
        
        if sameTree(root, subRoot): # they both exist now, so are they the same tree?
            return True
        
        # if they arent the same tree, check if it is a subtree of the left subtree of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




