/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const charArr = s.replace(/\s+/g, '').toLowerCase().replace(/[^a-z0-9]/g, '').split('')
    let left = 0
    let right = charArr.length - 1
    if(charArr.length == 0)
    {
        return true
    }

    while(left < right)
    {
        if(charArr[left] !== charArr[right])
        {
            return false
        }
        left++
        right--
    }

    return true
    
};