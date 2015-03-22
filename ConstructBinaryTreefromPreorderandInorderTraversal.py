# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        print preorder, inorder
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: index+1], inorder[0: index])
        root.right = self.buildTree(preorder[index+1:len(preorder)], inorder[index+1:len(inorder)])

        return root

if __name__ == '__main__':
    preorder = [1, 2, 3, 4, 5, 6, 7]
    inorder = [3, 2, 4, 1, 6, 5, 7]
    res = inorder.index(preorder[0])
    solution = Solution()
    res = solution.buildTree(preorder, inorder)
    print res
