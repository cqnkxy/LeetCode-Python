# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right and sum == root.val:
                ret.append(path[:])
            dfs(root.left, sum-root.val)
            dfs(root.right, sum-root.val)
            path.pop()

        ret, path = [], []
        dfs(root, sum)
        return ret


class Solution2(object):
    def pathSum(self, root, total):
        stk, ans = [], []
        while stk or root:
            if root:
                total -= root.val
                stk.append((root, False, total))
                root = root.left
            else:
                cur, twice, total = stk.pop()
                if twice:
                    if not (cur.left or cur.right) and total == 0:
                        ans.append([node.val for node, _, _ in stk] + [cur.val])
                else:
                    stk.append((cur, True, total))
                    root = cur.right
        return ans
