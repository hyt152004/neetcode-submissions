# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # use a queue

        # for every level, append the last element of the queue in to result

            # for every element in this level, add the children

        if not root:
            return []

        q = deque([root])
        # list of values
        result = []

        while q:
            rightNode = None
            for i in range(len(q)):
                qNode = q.popleft()

                if qNode:
                    rightNode = qNode
                    q.append(qNode.left)
                    q.append(qNode.right)

            if rightNode:
                result.append(rightNode.val)

        return result










            

        