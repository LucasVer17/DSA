/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const set = new Set(nums1)
    const returnSet = new Set()
    for(num of nums2)
    {
        if(set.has(num))
        {
            returnSet.add(num)
        }
    }
    return Array.from(returnSet)

};