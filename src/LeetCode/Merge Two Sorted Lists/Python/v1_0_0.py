#/]: # ( ------------------------------------------------------------------ {c)
#/]: # ( COPYRIGHT 2022 Dwij Bavisi <dwijbavisi@gmail.com>                  {c)
#/]: # ( Licensed under:                                                    {c)
#/]: # (     Taciturn Coder's `License to Hack` License                     {c)
#/]: # (     TC's L2H 1.0                                                   {c)
#/]: # ( A copy of the License may be obtained from:                        {c)
#/]: # (     https://TaciturnCoder.github.io/TCsL2H/legalcode/1.0           {c)
#/]: # ( See the License for the permissions and limitations.               {c)
#/]: # ( ------------------------------------------------------------------ {c)

# # Merge Two Sorted Lists
# Shrutajnana (version:1, patch:0, draft:0)

# Original problem available at: https://leetcode.com/problems/merge-two-sorted-lists/

# ---
# ## Problem statement
# Available here: [Problem.md](../Problem.md)

# ## Version 1.0.0
# Time complexity | Space complexity | Notes |
# | --- | --- | --- |
# | O(n) | O(1) |  |

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        head1 = list1
        head2 = list2

        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        tail = head

        while head1:
            if head2 == None:
                tail.next = head1
                break

            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next

            tail = tail.next
            pass

        if head2:
            tail.next = head2

        return head
