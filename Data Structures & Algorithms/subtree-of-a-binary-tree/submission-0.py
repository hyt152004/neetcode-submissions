# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None:
            return False

        if subRoot == None:
            return True

        if self.checkSubtree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def checkSubtree(self, root, subRoot) -> bool:
        if root == None and subRoot == None:
            return True

        if (subRoot == None and root != None) or (subRoot != None and root == None):
            return False

        if root.val != subRoot.val:
            return False

        print(str(root.val) + " equals " + str(subRoot.val))

        return self.checkSubtree(root.left, subRoot.left) and self.checkSubtree(root.right, subRoot.right)

        






