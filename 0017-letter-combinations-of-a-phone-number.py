"""
17. Letter Combinations of a Phone Number
Medium
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    "2": "abc"
    "3": "def"
    "4": "ghi"
    "5": "jkl"
    "6": "mno"
    "7": "pqrs"
    "8": "tuv"
    "9": "wxyz"

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
from typing import List


class Solution:
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if digits:
            self.dfs(digits, 0, [], combinations)
        return combinations

    def dfs(self, digits: str, index: int, combination: List[str], combinations: List[List[str]]):
        if index == len(digits):
            combinations.append("".join(combination))
            return

        for letter in self.letters[digits[index]]:
            combination.append(letter)
            self.dfs(digits, index+1, combination, combinations)
            combination.pop()


if __name__ == "__main__":
    digits = "23"
    output = Solution().letterCombinations(digits)
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    digits = ""
    output = Solution().letterCombinations(digits)
    expected = []

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)

    digits = "2"
    output = Solution().letterCombinations(digits)
    expected = ["a", "b", "c"]

    status = True
    for o in output:
        if o not in expected:
            status = False
            break

    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(status)
