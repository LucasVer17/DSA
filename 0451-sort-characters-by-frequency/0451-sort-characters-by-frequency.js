/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    const map = new Map()
    for(ch of s)
    {
        map.set(ch, (map.get(ch) || 0) + 1)
    }
    const arrayEntradas = [...map.entries()]
    arrayEntradas.sort((a, b) => b[1] - a[1])
    let resultado = ""
    for([key, value] of arrayEntradas)
    {
        resultado += key.repeat(value)
    }

    return resultado
};