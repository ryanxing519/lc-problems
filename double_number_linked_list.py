# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def double(node):
            if node:
                new = node.val * 2 + double(node.next)
                node.val = new % 10
                return new // 10
            return 0

        if double(head):
            newHead = ListNode(val=1, next=head)
            return newHead
        return head
