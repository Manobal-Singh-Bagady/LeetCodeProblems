# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        a1 = ans
        while l1 is not None or l2 is not None or carry == 1:
            a = l1.val if l1 is not None else 0
            b = l2.val if l2 is not None else 0
            temp = a + b + carry
            if temp >= 10:
                carry = 1
            else:
                carry = 0
            a1.val = temp % 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            a1.next = ListNode() if l1 is not None or l2 is not None or carry!=0 else None
            a1 = a1.next
            
        return ans