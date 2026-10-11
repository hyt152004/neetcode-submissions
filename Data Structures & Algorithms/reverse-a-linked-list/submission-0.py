# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        rsf = None

        while head != None:
            temp_head = head
            head = head.next

            temp_head.next = rsf
            rsf = temp_head



        return rsf

