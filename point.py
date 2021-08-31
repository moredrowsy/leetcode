class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self) -> str:
        return f"{self.x}:{self.y}"

    def __str__(self) -> str:
        return f"{self.x}:{self.y}"

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y if o else False
