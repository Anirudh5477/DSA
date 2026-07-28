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
        if not head:
            return None

        curr = head
        while curr:
            nxt = curr.next
            curr.next = Node(curr.val, nxt)
            curr = nxt
        curr = head
        ans = new = curr.next
        while curr.next:
            new.random=curr.random.next if curr.random else None
            curr = curr.next.next
            if curr is None:
                break
            new.next = new.next.next
            new = new.next
        return ans
        

        