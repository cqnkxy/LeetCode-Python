# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        diff, ans = abs(root.val-target), root.val
        while root:
            if diff > abs(root.val-target):
                diff, ans = abs(root.val-target), root.val
            root = root.left if root.val > target else root.right
        return ans
