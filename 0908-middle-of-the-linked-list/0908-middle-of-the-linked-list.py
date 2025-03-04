# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head

        while hare and hare.next:
            tortoise = tortoise.next  # Move tortoise by 1 step
            hare = hare.next.next     # Move hare by 2 steps

        return tortoise
        