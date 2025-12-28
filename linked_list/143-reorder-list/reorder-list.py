# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(reversehead):
            curr = reversehead
            prev = None
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr =nxt
            return prev
        # Split into two halves
        first = head
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        # reverse the second half
        rev_second = reverse(second)

        # merge first and reversed second together
        while rev_second:
            firstnxt = first.next
            secnxt = rev_second.next
            first.next = rev_second
            rev_second.next = firstnxt
            first = firstnxt
            rev_second=secnxt
        
       

        

        
