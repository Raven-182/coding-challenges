# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        #find the middle of the linked list
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #middle of the list
        slow = slow.next

        #reverse this new list
        prev = None
        current = slow 
        while current:
            next = current.next
            current.next = prev
            prev = current 
            current = next 

        #reversed stored in prev
        #now calculate the twin sums prev and head
        second = prev
        first = head
        maxSum = first.val + second.val
        while second.next:
            first = first.next
            second = second.next
            twinSum = first.val + second.val
            maxSum = max(twinSum, maxSum)
            
        return maxSum
        



        
