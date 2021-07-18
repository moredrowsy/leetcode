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
        self.values = []
        self.value_indices = {}  # Map {key: index} for self.values

    def __repr__(self) -> str:
        return f"{self.values}"

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.value_indices:
            return False

        self.values.append(val)
        self.value_indices[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.value_indices:
            return False

        index = self.value_indices[val]
        # Update last item to index
        self.value_indices[self.values[-1]] = index
        self.values[index], self.values[-1] = self.values[-1], self.values[index]
        self.values.pop()
        del self.value_indices[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.values:
            return self.values[randint(0, len(self.values)-1)]
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
