Question:
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3




Answer:
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
    # listnode不太懂
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=head
        while p.next:
            if p.next.val==p.val:
                p.next=p.next.next
            else:
                p=p.next
        return dummy.next
