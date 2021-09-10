"""
570. Find the Missing Number II
Medium
https://www.lintcode.com/problem/570/

To give a random string sequence composed of 1 - n integers, in which an integer is lost, please dfs it.

NOTE
n < 100
Data guarantees have only one solution.
if the list that you've found has more than one missing numbers, which could be that you didn't dfs the correct way to split the string.
"""


class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, str):
        used = [False] * (n + 1)
        return self.dfs(n, str, 0, used)

    def dfs(self, n, str, index, used):
        if index == len(str):
            results = []

            for i in range(1, n + 1):
                if not used[i]:
                    results.append(i)

            return results[0] if len(results) == 1 else -1

        if str[index] == '0':
            return -1

        for l in range(1, 3):
            num = int(str[index: index + l])

            if num >= 1 and num <= n and not used[num]:
                used[num] = True

                target = self.dfs(n, str, index + l, used)
                if target != -1:
                    return target

                used[num] = False

        return -1


if __name__ == "__main__":
    n = 20
    string = "19201234567891011121314151618"
    output = Solution().findMissing2(n, string)
    expected = 17
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 6
    string = "56412"
    output = Solution().findMissing2(n, string)
    expected = 3
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
