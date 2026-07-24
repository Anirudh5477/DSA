# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            curr = list2
            _list2 = list2.next
            _list1 = list1
        else:
            curr = list1
            _list1 = list1.next
            _list2 = list2
        ans = curr
        while _list1 and _list2:
            if _list2.val>_list1.val:
                curr.next = _list1
                curr = curr.next
                _list1 = _list1.next
            else:
                curr.next= _list2
                curr = curr.next
                _list2 = _list2.next
        while _list1:
            curr.next = _list1
            curr = curr.next
            _list1 = _list1.next
        while _list2:
            curr.next = _list2
            curr = curr.next
            _list2 = _list2.next
        return ans


        