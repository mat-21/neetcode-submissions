"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cache = dict()

        def get_cache_item(item):
            if not item:
                return None
            if item not in cache:
                cache[item] = Node(x=item.val)
            return cache[item]

        curr = head
        new_head = None
        while curr:
            new = get_cache_item(curr)
            if not new_head:
                new_head = new
            
            if curr.next:
                new.next = get_cache_item(curr.next)
            if curr.random:
                new.random = get_cache_item(curr.random)
            curr = curr.next

        return new_head









