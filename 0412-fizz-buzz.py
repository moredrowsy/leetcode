"""
412. Fizz Buzz
Easy
https://leetcode.com/problems/fizz-buzz/

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Time Complexity
        ---------------
        O(n)

        Space Complexity
        ----------------
        O(n)
        """
        output = []

        for i in range(n):
            output.append("")
            num = i + 1

            is3 = num % 3 == 0
            is5 = num % 5 == 0

            if not is3 and not is5:
                output[i] += str(num)
            else:
                if is3:
                    output[i] += "Fizz"
                if is5:
                    output[i] += "Buzz"

        return output


if __name__ == "__main__":
    n = 3
    output = Solution().fizzBuzz(n)
    expected = ["1", "2", "Fizz"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 5
    output = Solution().fizzBuzz(n)
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    n = 15
    output = Solution().fizzBuzz(n)
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
                "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
