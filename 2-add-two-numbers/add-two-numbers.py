# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values and carry
            total = val1 + val2 + carry

            # Calculate digit and carry
            digit = total % 10
            carry = total // 10

            # Create new node
            curr.next = ListNode(digit)
            curr = curr.next

            # Move to next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
        