/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const map = new Map()
    let count = 0
    let hasOdd = false
    for(let i = 0; i < s.length; i++)
    {
        if(!map.has(s[i]))
        {
            map.set(s[i], 1)
        }
        else
        {
            map.set(s[i], map.get(s[i]) + 1)
        }
    }

    for(let v of map.values())
    {
        if(v % 2 == 0)
        {
            count += v
        }
        else
        {
            count += v - 1
            hasOdd = true
        }
    }

    if(hasOdd) count += 1

    return count
};