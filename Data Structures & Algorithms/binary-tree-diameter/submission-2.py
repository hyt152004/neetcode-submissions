# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # need to has a rsf

        # add the height of left and right
        # update rsf

        # but this is too much of redundant work 

        # use dfs to avoid redundant work 
            # go all the way down, and move up
        rsf = 0

        def dfs(node):
            nonlocal rsf
            if not node:
                return 0

            # this will give the current height of this node starting from the bottom
            left = dfs(node.left)
            right = dfs(node.right)

            rsf = max(rsf, left + right)

            return 1 + max(left, right)
            
        dfs(root)

        return rsf
        













