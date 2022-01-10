# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]                            # to be able to access inside the below function
        def dfs(root):
            if not root:
                return -1                      # height of null tree, for single node its 0
            left = dfs(root.left)                                   # call it for root.left
            right = dfs(root.right)                                # call it for root.right      
            res[0] = max(res[0], 2 +left + right)         #updating it to the max value
            return 1+max(left, right)                    # height running through the root
        dfs(root)                                       # call it for root
        return res[0]                                  # returning the maximum value