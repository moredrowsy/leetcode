"""
1879. Two Sum VII
Hard
https://www.lintcode.com/problem/1879/

Given an array of integers that is already sorted in ascending absolute order,
find two numbers that the sum of them equals a specific number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Note: the subscript of
the array starts with 0

You are not allowed to sort this array.

Challenge
O(n) time complexity and O(1) extra space

Constraints:
 - It is guaranteed that all numbers in the numsnums is distinct.
 - The length of nums is <= 100 000
 - The number in nums is <= 10^9
"""


class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """

    def next_left(self, left, nums):
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(1)
        """
        n = len(nums)

        # In negative range, find next smallest negative or positive
        if nums[left] < 0:
            # Find next smallest negative
            for i in range(left-1, -1, -1):
                if nums[i] < 0:
                    return i
            # Couldn't find negative, find positive/0
            for i in range(n):
                if nums[i] >= 0:
                    return i
            # Couldn't find anything
            return -1
        # In positive/0 range, next smallest is positive
        else:
            for i in range(left+1, n):
                if nums[i] >= 0:
                    return i
            # Couldn't find anything
            return -1

    def next_right(self, right, nums):
        n = len(nums)

        # In positive range, find next largest positive or negative
        if nums[right] > 0:
            # Find next largest positive
            for i in range(right-1, -1, -1):
                if nums[i] > 0:
                    return i
            # Couldn't find any positive, find negative/0
            for i in range(n):
                if nums[i] <= 0:
                    return i
            # Couldn't find anything
            return -1
        # In negative/0 range, find next largest negative/0
        else:
            for i in range(right+1, n):
                if nums[i] <= 0:
                    return i
            # Couldn't find anything
            return -1

    def twoSumVII(self, nums, target):
        results = []

        if nums:
            left, right = 0, 0

            # Find global min left and max right
            for i in range(len(nums)):
                if nums[i] < nums[left]:
                    left = i
                if nums[i] > nums[right]:
                    right = i

            while nums[left] < nums[right]:
                lr_sum = nums[left] + nums[right]

                if lr_sum < target:
                    left = self.next_left(left, nums)
                elif lr_sum > target:
                    right = self.next_right(right, nums)
                else:
                    tmp = [left, right]

                    # Constraints: left index < right index
                    if left > right:
                        tmp[0], tmp[1] = tmp[1], tmp[0]

                    results.append(tmp)

                    left = self.next_left(left, nums)
                    right = self.next_right(right, nums)

                if left == -1 or right == -1:
                    break

        return results


if __name__ == "__main__":
    nums, target = [0, -1, 2, -3, 4], 1
    answer = Solution().twoSumVII(nums, target)
    print(answer)

    nums, target = [1, 2, 3, 4], 5
    answer = Solution().twoSumVII(nums, target)
    print(answer)

    nums, target = [1, 4, 24, -30, -35, 35, -39, -46, -53, 65, -69, -70, -95,
                    96, 109, 124, 131, 143, 150, -163, -188, 189, -190, 245,
                    246, 266, -266, 272, 286, -296], 538
    answer = Solution().twoSumVII(nums, target)
    print(answer)

    nums, target = [11, -14, -23, -24, 27, -36, 48, 66, -70, -72], -60
    answer = Solution().twoSumVII(nums, target)
    print(answer)
