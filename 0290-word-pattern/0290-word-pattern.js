/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const charToWord = new Map()
    const wordToChar = new Map()
    s = s.split(" ")
    pattern = pattern.split('')
    

    if(pattern.length !== s.length)
    {
        return false
    }

    for(let i = 0; i < pattern.length; i++)
    {
        if(!charToWord.has(pattern[i]) && !wordToChar.has(s[i]))
        {
            charToWord.set(pattern[i], s[i])
            wordToChar.set(s[i], pattern[i])
        }
        else if(charToWord.has(pattern[i]))
        {
            if(charToWord.get(pattern[i]) !== s[i])
            {
                return false
            }
        }
        else if(wordToChar.has(s[i]))
        {
            if(wordToChar.get(s[i]) !== pattern[i])
            {
                return false
            }
        }

    }

    return true

};