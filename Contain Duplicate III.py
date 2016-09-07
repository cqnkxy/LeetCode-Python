# https://discuss.leetcode.com/topic/27608/java-python-one-pass-solution-o-n-time-o-n-space-using-buckets
"""n-t, n, n+t will be mapped into the same bucket.
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        dic, w = {}, t+1
        for idx, num in enumerate(nums):
            if idx > k:
                del dic[nums[idx-k-1]/w]
            bucket = num / w
            if bucket in dic:
                return True
            if bucket-1 in dic and num-dic[bucket-1] <= t:
                return True
            if bucket+1 in dic and dic[bucket+1]-num <= t:
                return True
            dic[bucket] = num
        return False
