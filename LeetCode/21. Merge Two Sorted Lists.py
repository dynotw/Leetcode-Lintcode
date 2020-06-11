Question:
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4



Answer:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # they are listnodes rather than lists
        ret = ListNode(0)
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val < l2.val:
            # l1.val为什么是第一个指针域？
           
            ret = l1
            ret.next = self.mergeTwoLists(l1.next,l2)
            # .next 把节点往后挪了一个，从第二个指针域开始比较
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l2.next,l1)

        return ret
