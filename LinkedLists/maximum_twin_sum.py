"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.
Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"mid: {slow.val}")
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        mid = prev

        slow = head
        max_sum = 0
        while mid:
            t1 = slow.val
            slow = slow.next
            t2 = mid.val
            mid = mid.next

            max_sum = max(max_sum, t1+t2)
        return max_sum

    def pairSum_list(arr):
        i = 0
        j = -1
        s = 0
        while i < len(arr)//2:
            s = max(s, arr[i]+arr[j])
            i += 1
            j -= 1
        print(f"Sum is {s}")
        return s




if __name__ == "__main__":
    # head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    head_1 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    head_2 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    # l = [7,57,13,31,17,65,32,3,97,22,7,20,69,35,69,75,13,33,50,80,64,71,15,28,2,27,39,48,13,22,84,5,51,46,26,78,56,63]
    l = [7,57,13,31,17,65,32,3,97,22,7,20,69,35,69,75,13,33,50,80,64,71,15,28,2,27,39,48,13,22,84,5,51,46,26,78,56,63]
    head = ListNode(l[0])
    head_3 = head
    for i in l[1:]:
        head.next = ListNode(i)
        head = head.next


    print(Solution.pairSum_list(l))

    max_sum = Solution().pairSum(head_2)
    print(max_sum)


