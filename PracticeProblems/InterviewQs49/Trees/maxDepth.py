#find the maximum depth of a given unsorted binary tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#this fucntion uses recursion to find the max depth, ckecking both the left and right side, if the right or left side has no root,
#0 is returned which stops makes the other the max until we are able to return the longest
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
        


