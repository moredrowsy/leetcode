"""
1375. Substring With At Least K Distinct Characters
Medium
https://www.lintcode.com/problem/1375/

Given a string S with only lowercase characters.

Return the number of substrings that contains at least k distinct characters.

Constraints:
- 10≤length(S)≤1,000,000
- 1 ≤ k ≤ 261≤k≤26
"""


class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        total_substrings = 0

        right = 0
        counter_map = {}

        n = len(s)
        for left in range(n):
            while right < n and len(counter_map) < k:
                if s[right] in counter_map:
                    counter_map[s[right]] += 1
                else:
                    counter_map[s[right]] = 1

                right += 1

            if len(counter_map) == k:
                total_substrings += n - right + 1

            counter_map[s[left]] -= 1
            if counter_map[s[left]] == 0:
                del counter_map[s[left]]

        return total_substrings

    def kDistinctCharacters1(self, s, k):
        left = 0
        count = 0
        counter_map = {}

        for right in range(len(s)):
            if s[right] in counter_map:
                counter_map[s[right]] += 1
            else:
                counter_map[s[right]] = 1

            while left <= right and len(counter_map) >= k:
                counter_map[s[left]] -= 1
                if counter_map[s[left]] == 0:
                    del counter_map[s[left]]
                left += 1

            if len(counter_map) == k - 1:
                count += left

        return count

    def bruteforce(self, str, k):
        """
        Sliding windows

        Time Complexity
        ---------------
        O(n^3)

        Space Complexity
        ----------------
        O(n)
        """
        n = len(str)
        if k > n:
            return 0

        substr_count = 0

        for l in range(k-1, n):
            left, right = 0, l
            while right < n:
                unique = set()
                for i in range(left, right+1):
                    unique.add(str[i])

                if len(unique) >= k:
                    substr_count += 1

                left += 1
                right += 1

        return substr_count


if __name__ == "__main__":
    # S, k = "abcabcabca", 4
    # output = Solution().kDistinctCharacters(S, k)
    # expected = 0
    # print(f"\noutput\t\t{output}")
    # print(f"expected\t{expected}")
    # print(output == expected)

    S, k = "abcabcabcabc", 3
    output = Solution().kDistinctCharacters(S, k)
    expected = 55
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    S, k = "veunvywzrejbyawhzkwzraafgdjoefevaczcjfdknpjdyqhttizpngweiqefbdtzgizxwfvaakeglpldjelvdbuhwcgkjnyzlxsz", 1
    output = Solution().kDistinctCharacters(S, k)
    expected = 5050
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
