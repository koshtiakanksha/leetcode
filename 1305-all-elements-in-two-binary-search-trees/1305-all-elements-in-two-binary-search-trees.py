# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(r: TreeNode):  # we define a new function that takes r treenode as arg
            return inorder(r.left) + [r.val] + inorder(r.right) if r else [] # add all of them
        
        return sorted(inorder(root1) + inorder(root2)) # call function for both and sort
    
    # time complexity= O(M+N)
    # Space complexity = O(M+N)