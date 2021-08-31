"""
895. Maximum Frequency Stack
Hard
https://leetcode.com/problems/maximum-frequency-stack/

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
 - void push(int val) pushes an integer val onto the top of the stack.
 - int pop() removes and returns the most frequent element in the stack.
    - If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.
"""
from collections import defaultdict
import heapq


class FreqStack:
    """
    Using dict to map values.

    Time Complexity
    ---------------
    O(log n)

    Space Complexity
    ----------------
    O(n)
    """

    def __init__(self):
        self.heap = []
        self.dict = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.dict[val] += 1
        self.index += 1
        heapq.heappush(self.heap, (-self.dict[val], -self.index,  val))

    def pop(self) -> int:
        if self.heap:
            _, _, val = heapq.heappop(self.heap)
            self.dict[val] -= 1
            return val
        return None


def process_problem(cmds, args):
    output = []
    freq_stack = None
    for cmd, arg in zip(cmds, args):
        result = None

        if cmd == "FreqStack":
            freq_stack = FreqStack()
        elif cmd == "pop":
            result = freq_stack.pop()
        elif cmd == "push":
            freq_stack.push(arg[0])

        output.append(result)

    return output


if __name__ == "__main__":
    cmds = ["FreqStack", "push", "push", "push", "push",
            "push", "push", "pop", "pop", "pop", "pop"]
    args = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    output = process_problem(cmds, args)
    expected = [None, None, None, None, None, None, None, 5, 7, 5, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    cmds = ["FreqStack", "push", "push", "push", "push", "push", "push", "push", "push",
            "push", "push", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop"]
    args = [[], [5], [1], [2], [5], [5], [5], [1], [6], [
        1], [5], [], [], [], [], [], [], [], [], [], []]
    output = process_problem(cmds, args)
    expected = [None, None, None, None, None, None, None,
                None, None, None, None, 5, 5, 1, 5, 1, 5, 6, 2, 1, 5]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    cmds = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "push",
            "pop", "push", "pop", "push", "pop", "push", "pop", "pop", "pop", "pop", "pop", "pop"]
    args = [[], [4], [0], [9], [3], [4], [2], [], [6],
            [], [1], [], [1], [], [4], [], [], [], [], [], []]
    output = process_problem(cmds, args)
    expected = [None, None, None, None, None, None, None, 4,
                None, 6, None, 1, None, 1, None, 4, 2, 3, 9, 0, 4]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
