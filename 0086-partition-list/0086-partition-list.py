class Solution:
    def partition(self, head, x):
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)
        
        before = before_dummy
        after = after_dummy
        
        current = head
        
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        after.next = None
        before.next = after_dummy.next
        
        return before_dummy.next