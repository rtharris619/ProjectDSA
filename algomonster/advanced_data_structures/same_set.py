class SameSet:
    def __init__(self) -> None:
        # parent[x] is the element directly above x in the tree
        self.parent = {}
        self.rank = {}

    def find(self, x) -> int:
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if rx not in self.rank:
            self.rank[rx] = 0
        if ry not in self.rank:
            self.rank[ry] = 0
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

    def is_same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
def driver():
    dsu = SameSet()
    dsu.merge(3, 1)
    dsu.merge(1, 0)
    dsu.merge(5, 4)
    print(dsu.is_same(3, 0))
    print(dsu.is_same(5, 0))
    