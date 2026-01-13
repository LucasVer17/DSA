/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int *arr = malloc(2 * sizeof(int));
    int last = numbersSize - 1, i = 0;
    while(i < last)
    {
        int sum = numbers[i] + numbers[last];
        if(sum > target)
        {
            last--;
        }
        else if(sum < target)
        {
            i++;
        }
        else if(sum == target)
        {
            arr[0] = i + 1;
            arr[1] = last + 1;
            *returnSize = 2;
            return arr;
        }
    }

    *returnSize = 0;
    return NULL;
}