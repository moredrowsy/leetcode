"""
960. First Unique Number in Data Stream II
Medium
https://www.lintcode.com/problem/960/

We need to implement a data structure named DataStream. There are two methods required to be implemented:

void add(number) // add a new number
int firstUnique() // return first unique number

NOTE
You can assume that there must be at least one unique number in the stream when calling the firstUnique.
"""

from collections import defaultdict


class DataStream:
    """
    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(n)
    """

    def __init__(self):
        self.nums = []
        self.counts = defaultdict(int)

    def add(self, num):
        """
        @param num: next number in stream
        @return: nothing
        """
        self.nums.append(num)
        self.counts[num] += 1

    def firstUnique(self):
        """
        @return: the first unique number in stream
        """
        for num in self.nums:
            if self.counts[num] == 1:
                return num
        return None


def parse_args(args):
    data_stream = DataStream()
    first_uniques = []

    import io
    buf = io.StringIO(args)
    lines = buf.readlines()

    for line in lines:
        arg = line.strip()
        if arg:
            if arg == "firstUnique()":
                first_uniques.append(data_stream.firstUnique())
            elif "add" in arg:
                num = int(arg[arg.find('(')+1:arg.rfind(')')])
                data_stream.add(num)

    return first_uniques


if __name__ == "__main__":
    args = """
    add(1)
    add(2)
    firstUnique()
    add(1)
    firstUnique()
    """
    output = parse_args(args)
    expected = [1, 2]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    args = """
    add(1)
    add(2)
    add(3)
    add(4)
    add(5)
    firstUnique()
    add(1)
    firstUnique()
    add(2)
    firstUnique()
    add(3)
    firstUnique()
    add(4)
    firstUnique()
    add(5)
    add(6)
    firstUnique()
    """
    output = parse_args(args)
    expected = [1, 2, 3, 4, 5, 6]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
