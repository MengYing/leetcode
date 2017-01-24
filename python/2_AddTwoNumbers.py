#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answerRef = ListNode(0)
        total, carry = answerRef, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val // 10, val % 10
            total.next = ListNode(val)
            total = total.next

        if carry == 1:
            total.next = ListNode(1)

        return answerRef.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

# if __name__ == '__main__':
#     l1, l1.next, l1.next.next = ListNode(9), ListNode(9), ListNode(9)
#     l2, l2.next, l2.next.next = ListNode(9), ListNode(9), ListNode(9)
#     result = Solution().addTwoNumbers(l1, l2)
#     while result:
#         print result.val
#         result = result.next
