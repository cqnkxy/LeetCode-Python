class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def _dfs(word, path, ans, cnt):
            if not word:
                ans.append(path if not cnt else path+str(cnt))
            else:
                if cnt:
                    _dfs(word[1:], path+str(cnt)+word[0], ans, 0)
                else:
                    _dfs(word[1:], path+word[0], ans, 0)
                _dfs(word[1:], path, ans, cnt+1)
            return ans
        return _dfs(word, '', [], 0)


class Solution2(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def dfs(word, path, ans=[]):
            if not word:
                ans.append(re.sub('\d+', lambda m: str(len(m.group())), path))
                return ans
            dfs(word[1:], path+'1')
            dfs(word[1:], path+word[0])
            return ans
        return dfs(word, '')


if __name__ == '__main__':
    solution = Solution()
    print solution.generateAbbreviations('word')
