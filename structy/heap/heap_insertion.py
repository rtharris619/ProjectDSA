# Implement the insert method for the existing class.
# The method should properly add a given value into the heap, maintaining min heap order and height balance.

# It's important to keep the tree Complete.
# You can use a list to store the heap values.

# From the perspective of the parent node:
# parent:       i
# left child:   2i + 1
# right child:  2i + 2

# From the perspective of the child node:
# child: i
# parent: floor((i - 1) / 2)

# Method:
# Add new node to the left-most position of the bottom level.
# Sift up the new node while its less than its parent.

class MinHeap:
    def __init__(self):
        self.list = []
        
    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def _swap(self, idx_1, idx_2):
        self.list[idx_1], self.list[idx_2] = self.list[idx_2], self.list[idx_1]

    def _sift_up(self, idx):
        current_idx = idx
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
            if self.list[current_idx] < self.list[parent_idx]:
                self._swap(current_idx, parent_idx)
                current_idx = parent_idx
            else:
                break
        
    def insert(self, val):
        self.list.append(val)
        self._sift_up(len(self.list) - 1)

def driver():
    heap = MinHeap()
    heap.insert(12)
    heap.insert(13)
    heap.insert(11)
    heap.insert(4)
    heap.insert(20)
    heap.insert(9)
    heap.insert(22)
    heap.insert(14)

    print(heap.list)

    #
    #               4
    #            /    \
    #          11      9
    #         / \    /  \
    #       13  20  12  22
    #      /
    #    14
    #
    # [ 4, 11, 9, 13, 20, 12, 22, 14 ]
