# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret, lvl = [], [root] if root else []
        dirc = 1
        while lvl:
            ret += [node.val for node in lvl[::dirc]],
            lvl = [child for node in lvl for child in (node.left, node.right) if child]
            dirc = -dirc
        return ret
