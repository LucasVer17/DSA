/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    if(!list1) return list2;
    if(!list2) return list1;

    let curr = new ListNode();
    let start = curr;

    while(list1 && list2) {
        if(list1.val < list2.val) 
        {
            start.next = list1;
            list1 = list1.next;
        } 
        else 
        {
            start.next = list2;
            list2 = list2.next;
        }
        start = start.next;
    }
    if(!list1) start.next = list2;
    if(!list2) start.next = list1;

    return curr.next;
};