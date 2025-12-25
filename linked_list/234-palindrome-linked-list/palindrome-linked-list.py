# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        org = copy.deepcopy(head)

        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        while prev and org:
            
            if prev.val!=org.val:
                return False
            prev = prev.next
            org = org.next
        return True
        