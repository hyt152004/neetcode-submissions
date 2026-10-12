# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # use a queue data structure

        q = deque([root])

        result = []

        while q:
            subResult = []
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                q.append(node.left)
                q.append(node.right)

                subResult.append(node.val)
            if subResult:
                result.append(subResult)

        return result









        
        