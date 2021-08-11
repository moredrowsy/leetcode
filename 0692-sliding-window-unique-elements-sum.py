"""
692. Sliding Window Unique Elements Sum
Medium
https://www.lintcode.com/problem/692/

Given an array and a window size that is sliding along the array, find the sum of the count of unique elements in each window.

NOTE
If the window size is larger than the length of array, just regard it as the length of the array (left.e., the window won't slide).
"""


class Solution:
    """
    @param nums: the given array
    @param k: the window size
    @return: the sum of the count of unique elements in each window
    """

    def slidingWindowUniqueElementsSum(self, nums, k):
        total_unique = 0

        if nums and k > 0:
            right = 0
            unique_count = 0
            counter_map = {}

            n = len(nums)
            for left in range(n):
                while right < n and right - left < k:
                    if nums[right] in counter_map:
                        counter_map[nums[right]] += 1
                    else:
                        counter_map[nums[right]] = 1

                    # Count 1 is unique so inc
                    if counter_map[nums[right]] == 1:
                        unique_count += 1
                    # Count > 1 is not unique so dec
                    elif counter_map[nums[right]] == 2:
                        unique_count -= 1

                    right += 1

                total_unique += unique_count

                # When out of while loop, the window is too large > k
                # Next for loop will decrease window to k by removing a char
                # Thus, we need to decrement counter for nums[left] by one
                counter_map[nums[left]] -= 1

                # After we decrement, check to see if char is unique and inc
                # Also check if char exists; if not, dec unique counter
                if counter_map[nums[left]] == 1:
                    unique_count += 1
                elif counter_map[nums[left]] == 0:
                    unique_count -= 1

                if right == n:
                    break

        return total_unique


if __name__ == "__main__":
    nums, w = [1, 2, 1, 3, 3], 3
    output = Solution().slidingWindowUniqueElementsSum(nums, w)
    expected = 5
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, w = [1, 2, 1, 2, 1], 3
    output = Solution().slidingWindowUniqueElementsSum(nums, w)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, w = [1, 2, 1, 3, 3], 5
    output = Solution().slidingWindowUniqueElementsSum(nums, w)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, w = [1, 2, 1, 3, 3], 6
    output = Solution().slidingWindowUniqueElementsSum(nums, w)
    expected = 1
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    nums, w = [1, 1, 1, 1, 1], 2
    output = Solution().slidingWindowUniqueElementsSum(nums, w)
    expected = 0
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
