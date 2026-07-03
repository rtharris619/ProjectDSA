class UnionFind:
    def __init__(self, x: int):
        self.parent = list(range(x))

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        # apply path compression
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.parent[rx] = ry

    def get_parent(self):
        return self.parent
    
def driver():
    n = 5
    print("  node", list(range(n)))
    dsu = UnionFind(n)
    dsu.union(0, 1)
    dsu.union(1, 2)
    dsu.union(2, 3)
    dsu.union(3, 4)
    dsu.find(1)
    print("parent", dsu.get_parent())