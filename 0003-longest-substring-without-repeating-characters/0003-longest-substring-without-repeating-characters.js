/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const set = new Set()
    let count = 0
    let left = 0
    let maxLen = 0
    let right = 0
    while(right < s.length)
    {
        if(!set.has(s[right]))
        {
            set.add(s[right])
            right++
            count = right - left
        }
        else if(set.has(s[right]))
        {
            set.delete(s[left])
            left++
            count = 0
        }
    
        maxLen = Math.max(maxLen, count)
    }

    return maxLen
};