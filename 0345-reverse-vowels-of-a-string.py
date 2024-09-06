"""
345. Reverse Vowels of a String
Easy
https://leetcode.com/problems/reverse-vowels-of-a-string/

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(s)
        left, right = 0, n-1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        tmp = list(s)

        while left < right:
            while left <= right and not tmp[left] in vowels:
                left += 1
            while left <= right and not tmp[right] in vowels:
                right -= 1

            if left <= right:
                tmp[left], tmp[right] = tmp[right], tmp[left]

            left += 1
            right -=1

        return ''.join(tmp)

if __name__ == "__main__":
    s = "hello"
    output = Solution().reverseVowels(s)
    expected = "holle"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    s = ".,"
    output = Solution().reverseVowels(s)
    expected = ".,"
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

