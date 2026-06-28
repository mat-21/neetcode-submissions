# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head

        while curr and stack:
            last_item = stack.pop()
            
            if curr == last_item or curr.next == last_item:
                last_item.next = None
                break

            last_item.next = curr.next
            curr.next = last_item
            curr = curr.next.next
