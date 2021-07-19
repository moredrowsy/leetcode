"""
381. Insert Delete GetRandom O(1) - Duplicates allowed
Hard
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

Implement the RandomizedCollection class:

RandomizedCollection() Initializes the RandomizedCollection object.
 - bool insert(int val) Inserts an item val into the multiset if not present. Returns true if the item was not present, false otherwise.
 - bool remove(int val) Removes an item val from the multiset if present. Returns true if the item was present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
 - int getRandom() Returns a random element from the current multiset of elements (it's guaranteed that at least one element exists when this method is called). The probability of each element being returned is linearly related to the number of same values the multiset contains.

You must implement the functions of the class such that each function works in average O(1) time complexity.

Constraints:

-231 <= val <= 231 - 1
At most 2 * 105  calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
from random import randint


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.value_to_indices_map = {}  # Map of set indices

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.values.append(val)
        index = len(self.values) - 1

        if val in self.value_to_indices_map:
            self.value_to_indices_map[val].add(index)
            return False
        else:
            self.value_to_indices_map[val] = {index}
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.value_to_indices_map:
            return False

        # Value to remove
        value_indices_set = self.value_to_indices_map[val]
        value_index = next(iter(value_indices_set))

        # Value to replace
        replace_index = len(self.values) - 1
        replace_value = self.values[replace_index]
        replace_indices_set = self.value_to_indices_map[replace_value]

        # Replace
        self.values[value_index] = replace_value
        self.values.pop()

        # Update indices
        value_indices_set.remove(value_index)
        if not self.value_to_indices_map[val]:
            del self.value_to_indices_map[val]

        if replace_index in replace_indices_set:
            replace_indices_set.remove(replace_index)
            replace_indices_set.add(value_index)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.values:
            return self.values[randint(0, len(self.values)-1)]
        else:
            return None


def process_problem(cmds, args):
    output = []
    rand_col = None
    for cmd, arg in zip(cmds, args):
        result = None

        if cmd == "RandomizedCollection":
            rand_col = RandomizedCollection()
        elif cmd == "insert":
            result = rand_col.insert(arg[0])
        elif cmd == "remove":
            result = rand_col.remove(arg[0])
        elif cmd == "getRandom":
            result = rand_col.getRandom()

        output.append(result)

    return output


if __name__ == "__main__":
    from random import seed
    seed(0)

    cmds = ["RandomizedCollection", "insert", "insert",
            "insert", "getRandom", "remove", "getRandom"]
    args = [[], [1], [1], [2], [], [1], []]
    output = process_problem(cmds, args)
    expected = [None, True, False, True, 1, True, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    cmds = ["RandomizedCollection", "insert", "remove", "insert"]
    args = [[], [1], [1], [1]]
    output = process_problem(cmds, args)
    expected = [None, True, True, True]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    cmds = ["RandomizedCollection", "insert", "insert", "insert",
            "insert", "insert", "remove", "remove", "remove", "remove"]
    args = [[], [4], [3], [4], [2], [4], [4], [3], [4], [4]]
    output = process_problem(cmds, args)
    expected = [None, True, True, False, True, False, True, True, True, True]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)

    cmds = ["RandomizedCollection", "insert", "insert", "insert", "insert",
            "insert", "remove", "remove", "remove", "insert", "remove",
            "getRandom", "getRandom", "getRandom", "getRandom", "getRandom",
            "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
    args = [[], [1], [1], [2], [2], [2], [1], [1], [2], [1],
            [2], [], [], [], [], [], [], [], [], [], []]
    output = process_problem(cmds, args)
    expected = [None, True, False, True, False, False, True,
                True, True, True, True, 2, 1, 1, 1, 1, 1, 1, 2, 2, 1]
    print(f"\noutput\t\t{output}")
    print(f"expected\t{expected}")
    print(output == expected)
