class SetCounter:
    def __init__(self):
        self.parent = {}
        self.sizes = {}

    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            self.sizes[x] = 1
        if self.parent[x] == x:            
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        self.parent[rx] = ry
        self.sizes[ry] = self.sizes[rx] + self.sizes[ry]

    def count(self, x: int) -> int:
        return self.sizes[self.find(x)]
    
def driver():
    dsu = SetCounter()
    dsu.merge(1, 2)
    dsu.merge(2, 3)
    print(dsu.count(3))
    print(dsu.count(4))