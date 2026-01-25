/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    const seen = new Set();
    while (n !== 1) 
    {
        let total = 0;
        let x = n;


        while (x > 0) 
        {
            let d = x % 10;
            total += d * d;
            x = Math.floor(x / 10);
        }

        if (seen.has(total)) return false;

        seen.add(total);
        n = total;
    }


    return true;
};