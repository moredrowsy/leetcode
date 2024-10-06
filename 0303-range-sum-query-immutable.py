"""
303. Range Sum Query - Immutable
Easy
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
from typing import List

class NumArray:
  def __init__(self, nums: List[int]) -> None:
    if nums and len(nums) > 0:
      self.nums = nums
      self.prefix = self._prefix_sum(nums)

  def sumRange(self, left: int, right: int) -> int:
    if self.nums is None:
      return 0

    if left == 0:
      return self.prefix[right]

    return self.prefix[right] - self.prefix[left-1]

  def _prefix_sum(self, nums: List[int]):
    n = len(nums)
    prefix = [0] * n
    prefix[0] = nums[0]

    for i in range(1, n):
      prefix[i] = prefix[i-1] + nums[i]

    return prefix

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    args = [
      [0, 2],
      [2, 5],
      [0, 5]
    ]
    outputs = []
    for arg in args:
      output = numArray.sumRange(arg[0], arg[1])
      outputs.append(output)
    expected = [1, -1, -3]
    print(f"\noutput\t\t{outputs}")
    print(f"expected\t{expected}")
    print(outputs == expected)
