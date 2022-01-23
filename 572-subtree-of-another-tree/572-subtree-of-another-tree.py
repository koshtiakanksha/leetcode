# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:            # if subroot is none, we obv return True
            return True
        if not s:             # if tree is  None and subtree is not None, we return False
            return False
        if self.sameTree(s,t):     # we return true if it is true after caliing sameTree fun
            return True
        return (self.isSubtree(s.left, t)) or (self.isSubtree(s.right, t)) 
    
    # if we get false after calling the function, then we call it for left and right and return True if any one of them is True
        
        
# we def another function to check if subtree of tree and the given subtree are both equal
    
    def sameTree(self, s, t):   
        if not s and not t:                         # if none of then exists we return True
            return True
        if s and t and s.val==t.val:                # If both exits and heir values are same
            return (self.sameTree(s.left, t.left)) and (self.sameTree(s.right, t.right))
        return False   
    
    # we don't just want the root values to be same, we want the left and right node to be same and else we return False
    
        # time complexity = O(s*t)
        # space Complexity = O(1)