/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    let fast = head
    let slow = head
    while(fast != null && fast.next != null)
    {
        fast = fast.next.next
        slow = slow.next
    }

    let prev = null
    let cur = slow
    while(cur != null)
    {
        let next = cur.next
        cur.next = prev
        prev = cur
        cur =  next
    }

    let first = head
    let second = prev
    while(second.next != null)
    {
        let temp1 = first.next
        let temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2
    }
};