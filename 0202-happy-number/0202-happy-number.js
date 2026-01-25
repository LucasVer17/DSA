/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let resultado = n.toString().split("").map(Number);
    const set = new Set();


    while (true) 
    {
        let total = 0;

        for (let num of resultado) 
        {
            total += num ** 2;
        }
        
        if (total === 1) return true;

        if (set.has(total)) return false;

        set.add(total);
        resultado = total.toString().split("").map(Number);
    }
    return true
};