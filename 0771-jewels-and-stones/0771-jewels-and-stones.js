/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    const hash = new Map()
    jewels = jewels.split("")
    stones = stones.split("")
    let j = 0
    for(let i = 0; i < jewels.length; i++)
    {
        hash.set(jewels[i], 0)
        console.log(jewels[i])
    }

    for(stone of stones)
    {
        if(hash.has(stone))
        {
            hash.set(stone, hash.get(stone) + 1)
        }
    }

    for(v of hash.values())
    {
        j += v
    }

    return j
};