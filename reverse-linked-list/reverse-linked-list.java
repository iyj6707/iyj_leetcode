/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
    ListNode end = head;
    ListNode ans = null;

    while (head != null) {
        ans = new ListNode(head.val, ans);
        end.next = head.next;
        head = head.next;
    }

    return ans;
    }
}