# Implement the extract_min method for the existing class.
# The method should return and remove the smallest value in the heap, maintaining min heap order and height balance.

# 

from math import inf

class MinHeap:
    def __init__(self):
        self.list = []
        
    def is_empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)
    
    def swap(self, index_1, index_2):
        self.list[index_1], self.list[index_2] = self.list[index_2], self.list[index_1]
    
    def sift_up(self, index):
        current_index = index
        while current_index > 0:
            parent_index = (current_index - 1) // 2
            if self.list[current_index] < self.list[parent_index]:
                self.swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
        
    def insert(self, val):
        self.list.append(val)
        self.sift_up(self.size() - 1)

    def _sift_down(self, idx):
        current_idx = idx
        while current_idx < self.size() - 1:
            left_child_idx = 2 * current_idx + 1
            right_child_idx = 2 * current_idx + 2

            left_child_val = inf if left_child_idx >= self.size() else self.list[left_child_idx]
            right_child_val = inf if right_child_idx >= self.size() else self.list[right_child_idx]

            smaller_child_val = left_child_val if left_child_val < right_child_val else right_child_val
            smaller_child_idx = left_child_idx if left_child_val < right_child_val else right_child_idx

            if self.list[current_idx] > smaller_child_val:
                self.swap(current_idx, smaller_child_idx)
                current_idx = smaller_child_idx
            else:
                break
        
    def extract_min(self):
        if self.is_empty():
            return None
        if self.size() == 1:
            return self.list.pop()
        min_value = self.list[0]
        # remove the last item in the heap and move that value to the beginning of the heap.
        self.list[0] = self.list.pop()
        self._sift_down(0)
        return min_value

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
    print(heap.extract_min()) # -> 4
    print(heap.extract_min()) # -> 9
    print(heap.extract_min()) # -> 11

    print(heap.list)
