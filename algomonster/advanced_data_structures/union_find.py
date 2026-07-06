class UnionFind:
    # every element starts as its own root
    def __init__(self, n: int):
        self.parent = list(range(n))

    # find the root of x by walking parent pointers
    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    # merge the clusters containing x and y
    def union(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.parent[rx] = ry

def driver():
    n = 6
    print("  node", list(range(n)))
    dsu = UnionFind(n)
    dsu.union(3, 1)
    dsu.union(1, 0)
    dsu.union(5, 4)
    dsu.union(2, 0)
    print("parent", dsu.parent)