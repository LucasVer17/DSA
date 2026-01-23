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
    let middle = slow

    let prev = null
    let cur = middle.next
    middle.next = null
    let next = middle
    while(cur != null)
    {
        next = cur.next
        cur.next = prev
        prev = cur
        cur =  next
    }

    let first = head
    let second = prev
    while(second != null)
    {
        let temp1 = first.next
        let temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2
    }
};