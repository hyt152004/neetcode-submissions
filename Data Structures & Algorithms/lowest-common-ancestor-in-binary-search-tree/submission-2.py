# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use recursion

        # cases at a given node
        if not root:
            return None

        # 1. if the node itself is either p or q
            # node is the LCA
        if root == p or root == q:
            return root

        # 2. p is on the left and q is on the right 
            # or the other way around

            # the node LCA
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return root









