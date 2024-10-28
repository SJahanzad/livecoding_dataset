class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursive: T O(n), M O(n)
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
