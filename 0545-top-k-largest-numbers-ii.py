"""
545. Top k Largest Numbers II
Medium
https://www.lintcode.com/problem/545/

Implement a data structure, provide two interfaces:

add(number). Add a new number in the data structure.
topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.
"""
import heapq


class Solution:
    def __init__(self, k):
        """
        @param: k: An integer
        """
        self.k = k
        self.heap = []

    def add(self, num):
        """
        @param: num: Number to be added
        @return: nothing
        """
        heapq.heappush(self.heap, (-num, num))

    def topk(self):
        """
        @return: Top k element
        """
        nums = [heapq.heappop(self.heap)[1]
                for _ in range(min(self.k, len(self.heap)))]
        for num in nums:
            self.add(num)
        return nums


def parse_args(args):
    output = []
    solution = None

    import io
    buf = io.StringIO(args)
    lines = buf.readlines()

    for line in lines:
        arg = line.strip()
        if not arg:
            continue

        result = None

        nstr = arg[arg.find('(')+1:arg.rfind(')')]

        if "new Solution" in arg:
            solution = Solution(int(nstr))
        elif "add" in arg:
            solution.add(int(nstr))
        elif "topk" in arg:
            result = solution.topk()

        if result:
            output.append(result)

    return output


if __name__ == "__main__":
    args = """
    s = new Solution(3);
    s.add(3)
    s.add(10)
    s.topk()
    s.add(1000)
    s.add(-99)
    s.topk()
    s.add(4)
    s.topk()
    s.add(100)
    s.topk()    
    """
    output = parse_args(args)
    expected = [
        [10, 3],
        [1000, 10, 3],
        [1000, 10, 4],
        [1000, 100, 10]
    ]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    args = """
    s = new Solution(1);
    s.add(3)
    s.add(10)
    s.topk()
    s.topk()  
    """
    output = parse_args(args)
    expected = [
        [10],
        [10]
    ]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
