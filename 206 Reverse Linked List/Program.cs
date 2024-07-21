
//  * Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}
 
public class Solution {
    public ListNode ReverseList(ListNode head) {
        ListNode prev = null;
        ListNode next;
        ListNode node = head;

        while (node != null)
        {
            next = node.next;
            node.next = prev;
            prev = node;
            node = next;
        }

        return prev;
    }
}