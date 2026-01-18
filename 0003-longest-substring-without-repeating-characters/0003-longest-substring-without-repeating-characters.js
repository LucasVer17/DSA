/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const map = new Set()
    let count = 0
    let left = 0
    let maxLen = 0
    let right = 0
    while(right < s.length)
    {
        if(!map.has(s[right]))
        {
            map.add(s[right])
            right++
            count = right - left
        }
        else if(map.has(s[right]))
        {
            map.delete(s[left])
            left++
            count = 0
        }
    
        maxLen = Math.max(maxLen, count)
    }

    return maxLen
};