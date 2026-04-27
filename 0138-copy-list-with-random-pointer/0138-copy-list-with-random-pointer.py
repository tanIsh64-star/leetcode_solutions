
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        
        while curr:
            curr.next = curr.next.next
            copy_curr.next = copy_curr.next.next if copy_curr.next else None
            curr = curr.next
            copy_curr = copy_curr.next
        
        return copy_head