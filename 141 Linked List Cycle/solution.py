# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object): 
    def hasCycle(self, head): #solution O(n)
        """
        :type head: ListNode
        :rtype: bool
        """
        
        set_node= set()

        while head is not None:
            if head in set_node:
                return True
            set_node.add(head)
            head = head.next
        
        return False
    
    def hasCycle2(self, head):
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False