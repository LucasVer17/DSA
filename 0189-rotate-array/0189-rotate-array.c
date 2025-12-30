void rotate(int* nums, int numsSize, int k) {
    k = k % numsSize;
    int* res = (int*)malloc(numsSize * sizeof(int));
    
    for (int i = 0; i < numsSize; i++) {
        res[(i + k) % numsSize] = nums[i];
    }
    for (int i = 0; i < numsSize; i++) {
        nums[i] = res[i];
    }
    
    free(res);
}