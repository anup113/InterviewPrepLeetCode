'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        ret = ListNode()
        temp = ret

        carry = 0
        while l1 or l2:
            digit = carry
            if l1:
                digit += l1.val
            if l2:
                digit += l2.val

            if digit > 9:
                carry = 1
                digit = digit % 10
            else:
                carry = 0

            temp.next = ListNode(digit)

            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            temp.next = ListNode(carry)
            temp = temp.next
        return ret.next
