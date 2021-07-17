"""
380. Insert Delete GetRandom O(1)
Medium
https://leetcode.com/problems/insert-delete-getrandom-o1/

Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
 - bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
 - bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
 - int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.items = []
        self.indices = {}

    def __repr__(self) -> str:
        return f"{self.items}"

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indices:
            return False
        else:
            self.items.append(val)
            self.indices[val] = len(self.items) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.indices:
            index = self.indices[val]
            self.indices[self.items[-1]] = index  # Update last item to index
            self.items[index], self.items[-1] = self.items[-1], self.items[index]
            self.items.pop()
            del self.indices[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.items:
            return self.items[randint(0, len(self.items)-1)]
        else:
            return None


def process_problem(cmds, args):
    output = []
    rand_set = None
    for cmd, arg in zip(cmds, args):
        result = None

        if cmd == "RandomizedSet":
            rand_set = RandomizedSet()
        elif cmd == "insert":
            result = rand_set.insert(arg[0])
        elif cmd == "remove":
            result = rand_set.remove(arg[0])
        elif cmd == "getRandom":
            result = rand_set.getRandom()

        output.append(result)

    return output


if __name__ == "__main__":
    cmds = ["RandomizedSet", "insert", "remove", "insert",
            "getRandom", "remove", "insert", "getRandom"]
    args = [[], [1], [2], [2], [], [1], [2], []]
    output = process_problem(cmds, args)
    print(output)

    cmds = ["RandomizedSet", "insert", "insert",
            "remove", "insert", "remove", "getRandom"]
    args = [[], [0], [1], [0], [2], [1], []]
    output = process_problem(cmds, args)
    print(output)
