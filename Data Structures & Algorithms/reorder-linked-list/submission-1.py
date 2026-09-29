# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         
        #  2 4 6 8 
        #    s 
        #    f
        #      s
        #        f
        #        s   f
            
        #     8 6 
         
        #  2 8 4 6

        # split the list
        
        # slow and fast

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None

        # reverse the second linked list
        while second:
            temp = second.next     # 1. Save where to continue
            second.next = prev     # 2. Flip this node's arrow backward
            prev = second          # 3. Grow reversed portion
            second = temp          # 4. Move forward in original list

        # merge them

        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
            
            


