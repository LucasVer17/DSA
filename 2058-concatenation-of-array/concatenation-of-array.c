/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int newSize = 2 * numsSize;
    int *ans;
    ans = (int*)malloc(newSize * sizeof(int));

    for(int  i = 0; i < numsSize; i++)
    {
        ans[i] = nums[i];
        ans[i + numsSize] = nums[i];
    }

    *returnSize = newSize;
    return ans;
}