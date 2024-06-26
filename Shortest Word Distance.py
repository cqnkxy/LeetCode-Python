class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pre, pos, ans = None, -1, len(words)
        for idx, word in enumerate(words):
            if word in (word1, word2):
                if pre and pre != word:
                    ans = min(ans, idx-pos)
                pre, pos = word, idx
        return ans
