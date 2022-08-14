# https://leetcode.com/problems/add-two-numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum1multiplier = 1
        while True:
            if l1 == None:
                break
            sum1 = sum1 + l1.val * sum1multiplier
            sum1multiplier = sum1multiplier * 10
            l1 = l1.next
        sum2 = 0
        sum2multiplier = 1
        while True:
            if l2 == None:
                break
            sum2 = sum2 + l2.val * sum2multiplier
            sum2multiplier = sum2multiplier * 10
            l2 = l2.next
        total_sum = sum1 + sum2
        return self.createListNode(str(total_sum))
    
    # def reverseNumber(self, number):
    #     divider = 1
    #     reverse = 0
    #     while number:
    #         reverse = reverse + ((number % 10) / divider)
    #         number = number // 10
    #         divider = divider * 10
    #     return int(reverse * divider / 10)
    
    def reverseNumber(self, number):
        return str(number)[::-1]
    
    # def createListNode(self, integer):
    #     nextValue = None
    #     if integer == 0:
    #         return ListNode(val = 0, next = None)
    #     while integer:
    #         toRetNodes = ListNode(val = integer % 10, next = nextValue)
    #         integer = integer // 10
    #         nextValue = toRetNodes
    #     return toRetNodes
    
    def createListNode(self, integer):
        nextValue = None
        for i in integer:
            toRetNodes = ListNode(val = int(i), next = nextValue)
            nextValue = toRetNodes
        return toRetNodes