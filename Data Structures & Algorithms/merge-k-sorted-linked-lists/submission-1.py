# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptrs = [head for head in lists]

        has_items = True
        dummy = curr = ListNode()
        while has_items:
            min_val = float('infinity')
            min_idx = None
            # iter over all ptrs
            for i in range(len(ptrs)):
                if ptrs[i] and ptrs[i].val < min_val:
                    min_val = ptrs[i].val
                    min_idx = i
            if min_idx is not None:
                # get min add to new list
                curr.next = ListNode(val=min_val)
                curr = curr.next
                ptrs[min_idx] = ptrs[min_idx].next

            # check stop condition
            if min_idx is None:
                has_items = False
        return dummy.next