/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    if(root == null)
    {
        return []
    }

    let result = []
    let q = [root]

    while(q.length > 0)
    {
        levelSize = q.length
        lvl = []

        for(let i = 0; i < levelSize; i++)
        {
            n = q.shift()
            lvl.push(n.val)
            if(n.left)
            {
                q.push(n.left)
            }
            if(n.right)
            {
                q.push(n.right)
            }
        }
        result.push(lvl)
    }
    return result
};