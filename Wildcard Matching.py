class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):
            return False
        dp = [[False for x in range(len(p)+1)] for y in range(len(s)+1)]
        dp[0][0] = True
        for col in range(1, len(p)+1):
            dp[0][col] = p[col-1] == '*' and dp[0][col-1]
        for row in range(1, len(s)+1):
            for col in range(1, len(p)+1):
                if p[col-1] == '*':
                    dp[row][col] = dp[row][col-1] or dp[row-1][col]
                else:
                    dp[row][col] = dp[row-1][col-1] and (p[col-1] == '?' or p[col-1] == s[row-1])
        return dp[-1][-1]


class Solution2(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count('*') > len(s):
            return False
        dp = [[False for x in range(len(p)+1)] for y in range(2)]
        dp[0][0] = True
        for col in range(1, len(p)+1):
            dp[0][col] = p[col-1] == '*' and dp[0][col-1]
        pre, cur = 0, 1
        for row in range(1, len(s)+1):
            dp[cur][0] = False
            for col in range(1, len(p)+1):
                if p[col-1] == '*':
                    dp[cur][col] = dp[cur][col-1] or dp[pre][col]
                else:
                    dp[cur][col] = dp[pre][col-1] and (p[col-1] == '?' or p[col-1] == s[row-1])
            cur, pre = pre, cur
        return dp[pre][-1]


class Solution3(object):
    def isMatch(self, s, p):
        if len(p) - p.count('*') > len(s):
            return False
        dp = [True] + [False] * len(s)
        for ch in p:
            prev, dp[0] = dp[0], dp[0] and ch == '*'
            for idx in range(1, len(s)+1):
                _prev = dp[idx]
                if ch == '*':
                    dp[idx] = dp[idx-1] or dp[idx]
                else:
                    dp[idx] = prev and (ch == s[idx-1] or ch == '?')
                prev = _prev
        return dp[-1]

