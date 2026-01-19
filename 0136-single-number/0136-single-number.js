/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let x = 0
    for (let n of nums) {
        x ^= n
    }
    return x
};