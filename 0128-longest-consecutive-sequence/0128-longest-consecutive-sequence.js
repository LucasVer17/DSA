/**
 * @param {number[]} nums
 * @return {number}
 */ 
var longestConsecutive = function(nums) {
    const set = new Set(nums)
    let max = 1
    if(set.size == 0)
    {
        return 0
    }
    for(let num of set)
    {
         if (!set.has(num - 1)) 
        {
            current = num
            let length = 1
            while (set.has(current + 1)) 
            {
            
                current++
                length++    
                max = Math.max(max, length)
                
            }
        }

    }

    return max
};