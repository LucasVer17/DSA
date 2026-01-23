/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) 
{
    struct ListNode* prevNode = 0;
    struct ListNode* curNode = head;
    struct ListNode* nextNode = head;

    while(curNode != 0)
    {
        nextNode = nextNode->next;
        curNode->next = prevNode;
        prevNode = curNode;
        curNode = nextNode;
    }

    head = prevNode;
    return head;
}