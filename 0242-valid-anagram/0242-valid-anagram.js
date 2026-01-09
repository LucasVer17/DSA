var isAnagram = function(s, t) {

    s = s.toLowerCase().replace(/\s/g, "")
    t = t.toLowerCase().replace(/\s/g, "")

    if (s.length !== t.length) return false

    let count = new Map()

    for(c of s)
    {
        count.set(c, (count.get(c) || 0) + 1)
    }
    for(c of t)
    {
        if(!count.has(c)) return false
        count.set(c, count.get(c) - 1)
    }

    for(let v of count.values())
    {
        if(v !== 0) return false
    }

    return true

};
