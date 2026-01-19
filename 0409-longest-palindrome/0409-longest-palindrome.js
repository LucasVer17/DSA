/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
   const m = new Map();

    for (let i = 0; i < s.length; i++) {
        m.set(s[i], (m.get(s[i]) || 0) + 1);
    }

    let count = 0;
    let hasOdd = false;

    for (let v of m.values()) {
        if (v % 2 === 0) {
            count += v;
        } else {
            count += v - 1;
            hasOdd = true;
        }
    }

    if (hasOdd) count += 1;

    return count;
};