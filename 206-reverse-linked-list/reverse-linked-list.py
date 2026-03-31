# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        stack = []

        temp = head

        # push all nodes except the last node into stack
        while temp.next is not None:
            stack.append(temp)
            temp = temp.next

        head = temp

        # pop all the nodes and append to the linked list
        while stack:

            # append the top value of stack in list
            temp.next = stack.pop()

            temp = temp.next

        temp.next = None

        return head


        