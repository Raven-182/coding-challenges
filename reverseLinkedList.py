# Definition for singly-linked list.
from typing import Optional
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #1 should point to None
        prev = None
        #get 1
        current = head
        
        while current:
            next_node = current.next  # grab the 2 chain
            current.next = prev       # mak the 1 point to None
            prev = current            # 1 becomes previous
            current = next_node       # current now becomes the 2 chain
        
        return prev

