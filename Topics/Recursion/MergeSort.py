
def merge_sort(array):
    if len(array) > 1:
        midpoint = len(array) // 2
        left = array[:midpoint]
        right = array[midpoint:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = current_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                array[current_index] = left[left_index]
                left_index += 1
            else:
                array[current_index] = right[right_index]
                right_index += 1

            current_index += 1

        while left_index < len(left):
            array[current_index] = left[left_index]
            left_index += 1
            current_index += 1

        while right_index < len(right):
            array[current_index] = right[right_index]
            right_index += 1
            current_index += 1


def test():
    array = [-5, 20, 10, 3, 2, 0]
    merge_sort(array)
    print(array)
