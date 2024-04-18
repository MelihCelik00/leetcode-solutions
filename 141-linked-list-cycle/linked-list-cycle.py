# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if (head == None):
            return False
        if (head.next == None):
            return False

        visited = set()
        curr = head
        while curr:
            if curr.next in visited:
                return True
            else:
                visited.add(curr)
                curr = curr.next
        
        return False