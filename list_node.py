class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        return f"{self.val}"

    def __str__(self) -> str:
        return f"{self.val}"

    def __eq__(self, o: object) -> bool:
        return self.val == o.val if o else False
