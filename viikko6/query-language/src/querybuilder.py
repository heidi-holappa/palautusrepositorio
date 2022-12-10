from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or


class QueryBuilder:

    def __init__(self, stats):
        self.stack = QueryStack()
        self.stats = stats

    def playsIn(self, team: str):
        self.stack.push(PlaysIn(team))
        return self

    def hasAtLeast(self, value: int, type: str):
        self.stack.push(HasAtLeast(value, type))
        return self

    def hasFewerThan(self, value: int, type: str):
        self.stack.push(HasFewerThan(value, type))
        return self

    def build(self):
        if not self.stack.has_items():
            return All()
        items = []
        while self.stack.has_items():
            items.append(self.stack.pop())
        return And(*items)

    def oneOf(self, *args):
        queries = args
        self.stack.push(Or(*queries))
        return self


class QueryStack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def has_items(self):
        return bool(len(self.stack))
