# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return (self._isSymmetric(left.left, right.right)
                    and self._isSymmetric(left.right, right.left))
        return False