/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const set = new Set()
    let left = 0
    let maxLen = 0
    let right = 0
    while(right < s.length)
    {
        if(!set.has(s[right]))
        {
            set.add(s[right])
            right++
            maxLen = Math.max(maxLen, right - left)
        }
        else
        {
            set.delete(s[left])
            left++
        }
    
    }

    return maxLen
};