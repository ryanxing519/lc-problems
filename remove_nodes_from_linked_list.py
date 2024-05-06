# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = []

        cur = head
        while cur:
            while nodes and cur.val > nodes[-1].val:
                nodes.pop()
            nodes.append(cur)
            cur = cur.next

        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                nodes[i].next = None
            else:
                nodes[i].next = nodes[i + 1]

        return nodes[0]
