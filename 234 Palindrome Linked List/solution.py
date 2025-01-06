class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        value = []

        while head is not None:
            value.append(head.val)
            head = head.next

        for i,n in enumerate(value[:len(value)//2]):
            if n != value[-1-i]:
                return False
        return True