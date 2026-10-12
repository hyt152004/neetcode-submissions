# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        newLL = head
        while list1 and list2:
            if list1.val <= list2.val:
                print(list1.val)
                print(list2.val)
                temp = list1.next
                list1.next = None
                newLL.next = list1
                newLL = newLL.next
                list1 = temp

            else:
                
                temp = list2.next
                list2.next = None
                newLL.next = list2
                newLL = newLL.next
                list2 = temp

        if list1:
            newLL.next = list1
        if list2:
            newLL.next = list2



        return head.next
        