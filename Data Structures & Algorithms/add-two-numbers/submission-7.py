# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        rem = 0

        curr1, curr2 = l1, l2
        res_head = res = ListNode()
        while curr1 or curr2:
            val1 = 0
            val2 = 0
            if curr1:
                val1 = curr1.val
            if curr2:
                val2 = curr2.val
            val = val1 + val2 + rem
            print(f'{val1} + {val2} + {rem} = ', val)    
            if val > 9:
                val = val - 10
                rem = 1
                print('over 9', val, rem)
            else:
                rem = 0
            
            res.next = ListNode(val=val)
            res = res.next
            
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if rem:
            res.next = ListNode(val=rem)
        return res_head.next