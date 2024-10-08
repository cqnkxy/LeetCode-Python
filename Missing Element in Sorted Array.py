from typing import List


class Solution:
    "O(n)"

    def missingElement(self, nums: List[int], k: int) -> int:
        expected = nums[0]
        for num in nums:
            if expected == num:
                expected += 1
                continue
            missing_cnt = num - expected
            if missing_cnt >= k:
                break
            k -= missing_cnt
            expected = num + 1
        return expected + k - 1


class Solution2:
    "O(log(n))"

    def missingElement(self, nums: List[int], k: int) -> int:

        def missing_cnt(i: int) -> int:
            return nums[i] - nums[0] - i

        n = len(nums)
        if k > missing_cnt(n - 1):
            return nums[n - 1] + k - missing_cnt(n - 1)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if missing_cnt(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return nums[l - 1] + k - missing_cnt(l - 1)


if __name__ == '__main__':
    s = Solution()
    s2 = Solution2()
    print(s.missingElement([4, 7, 9, 10], k=1),
          s2.missingElement([4, 7, 9, 10], k=1))
    print(s.missingElement([4, 7, 9, 10], k=3),
          s2.missingElement([4, 7, 9, 10], k=3))
    print(s.missingElement([1, 2, 4], k=3), s2.missingElement([1, 2, 4], k=3))
