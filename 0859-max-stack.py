"""
859. Max Stack
Hard
https://www.lintcode.com/problem/859/

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
"""


class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if self.max_stack:
            number = max(self.max_stack[-1], x)
            self.max_stack.append(number)
        else:
            self.max_stack.append(x)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        return self.max_stack[-1]

    def popMax(self):
        max_number = self.peekMax()
        buffer_stack = []
        while self.top() != max_number:
            buffer_stack.append(self.pop())
        self.pop()
        while buffer_stack:
            self.push(buffer_stack[-1])
            buffer_stack.pop()
        return max_number


def process_problem(cmds):
    output = []
    maxstack = MaxStack()

    for cmd in cmds:
        result = None

        if "push" in cmd:
            cmd = cmd.replace("push(", "")
            cmd = cmd.replace(")", "")
            num = int(cmd)
            maxstack.push(num)
        elif cmd == "pop()":
            result = maxstack.pop()
        elif cmd == "top()":
            result = maxstack.top()
        elif cmd == "peekMax()":
            result = maxstack.peekMax()
        elif cmd == "popMax()":
            result = maxstack.popMax()

        if result:
            output.append(result)

    return output


if __name__ == "__main__":
    cmds = ["push(5)",
            "push(1)",
            "push(5)",
            "top()",
            "popMax()",
            "top()",
            "peekMax()",
            "pop()",
            "top()"]
    output = process_problem(cmds)
    expected = [5, 5, 1, 5, 1, 5]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
