# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        heightL = self.getHeight(root.left)
        heightR = self.getHeight(root.right)

        diff = abs(heightL - heightR)

        if diff > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)


        

    def getHeight(self, root):
        if root == None:
            return 0 

        return max(self.getHeight(root.left) + 1, self.getHeight(root.right) + 1)