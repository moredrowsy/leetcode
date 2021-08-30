"""
90. k Sum II
Medium
https://www.lintcode.com/problem/90/

Given n unique postive integers, number k (1<=k<=n1<=k<=n) and target.

Find all possible k integers where their sum is target.
"""


class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, nums, k, target):
        ksums = []
        self.dfs(nums, k, target, 0, [], ksums)
        return ksums

    def dfs(self, nums, k, target, index, ksum, ksums):
        if k == 0 and target == 0:
            ksums.append(ksum[:])
            return

        if k == 0 or target <= 0:
            return

        for i in range(index, len(nums)):
            ksum.append(nums[i])
            self.dfs(nums, k-1, target - nums[i], i+1, ksum, ksums)
            ksum.pop()


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 2
    target = 5
    output = Solution().kSumII(nums, k, target)
    expected = [[1, 4], [2, 3]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums = [1, 3, 4, 6]
    k = 3
    target = 8
    output = Solution().kSumII(nums, k, target)
    expected = [[1, 3, 4]]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
