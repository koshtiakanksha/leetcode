# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:     # if root1, root2 don't exist, don't return anything
            return None
        if root1:                       # if root 1 has a value, save it to a variable
            v1 = root1.val
        else:                           # else save the default value as 0
            v1 = 0
        if root2:
            v2 = root2.val
        else:
            v2 = 0
        root = TreeNode(v1 + v2)        # since we have to merge both trees
        
        root.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)                                   # call the function for root.left
        root.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)                              # and for root.right
        return root
        
        # time complexity O(m+n) 
        # m= no of elements in tree1 and n= no of elements in tree2