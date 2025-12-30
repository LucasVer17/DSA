int removeElement(int* nums, int numsSize, int val) {
    int left = 0;
    int end = numsSize - 1;

    while (left <= end) 
    {
        if (nums[left] == val) 
        {
            int temp = nums[left];
            nums[left] = nums[end];
            nums[end] = temp;
            end--;
        } else 
        {
            left++;
        }
    }

    return left;
}
