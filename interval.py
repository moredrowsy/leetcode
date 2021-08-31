class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        return f"{self.start}:{self.end}"

    def __str__(self) -> str:
        return f"{self.start}:{self.end}"

    def __eq__(self, o: object) -> bool:
        return self.start == o.start and self.end == o.end if o else False

    def __hash__(self) -> int:
        return id(self)
