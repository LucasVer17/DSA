/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    struct ListNode* devagar = head;
    struct ListNode* rapido = head;

    while(rapido != 0 && rapido->next != 0)
    {
        devagar = devagar->next;
        rapido = rapido->next->next;

        if(devagar == rapido)
        {
            return true;
        }
    }

    return false;

}