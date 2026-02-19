/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 * this.val = (val===undefined ? 0 : val)
 * this.left = (left===undefined ? null : left)
 * this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    const inorderMap = new Map();
    inorder.forEach((val, index) => inorderMap.set(val, index));

    function callRecursive(preStart, preEnd, inStart, inEnd) {
        if (preStart > preEnd || inStart > inEnd) return null;
        const rootVal = preorder[preStart];
        const root = new TreeNode(rootVal);
        const rootIndex = inorderMap.get(rootVal);
        const leftNodesCount = rootIndex - inStart;

        root.left = callRecursive(preStart + 1, preStart + leftNodesCount, inStart, rootIndex - 1);
        root.right = callRecursive(preStart + leftNodesCount + 1, preEnd, rootIndex + 1, inEnd);

        return root;
    }

    return callRecursive(0, preorder.length - 1, 0, inorder.length - 1);
};