"""
171. Anagrams
Medium

Given an array of strings, return all groups of strings that are anagrams.If a string is Anagram,there must be another string with the same letter set but different order in S.

Constraints:
 - All inputs will be in lower-case
"""


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        """
        Time Complexity
        ---------------
        O(n*klogk)

        Space Complexity
        ----------------
        O(n)
        """
        results = []

        if strs:
            anagrams = {}

            for i, word in enumerate(strs):
                word = "".join(sorted(word))

                if word in anagrams:
                    anagrams[word].append(i)
                else:
                    anagrams[word] = [i]

            for word in anagrams:
                if len(anagrams[word]) > 1:
                    results += [strs[i] for i in anagrams[word]]

        return results


if __name__ == "__main__":
    strs = ["lint", "intl", "inlt", "code"]
    output = Solution().anagrams(strs)
    expected = ["lint", "inlt", "intl"]
    output = sorted(output)
    expected = sorted(expected)
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    strs = ["ab", "ba", "cd", "dc", "e"]
    output = Solution().anagrams(strs)
    expected = ["ab", "ba", "cd", "dc"]
    output = sorted(output)
    expected = sorted(expected)
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
