from collections.abc import Callable


class Heap:
    """
    A generic Heap class, can be used as min or max by passing the key function
    accordingly.
    """

    def __init__(self, key: Callable | None = None) -> None:
        # Stores actual heap items.
        self.arr: list = []
        # Stores indexes of each item for supporting updates and deletion.
        self.pos_map: dict = {}
        # Stores current size of heap.
        self.size = 0
        # Stores function used to evaluate the score of an item on which basis ordering
        # will be done.
        self.key = key or (lambda x: x)

    def __repr__(self):
        return str([n[1] for n in self.arr])

    def _parent(self, i: int) -> int | None:
        """Returns parent index of given index if exists else None"""
        return int((i - 1) / 2) if i > 0 else None

    def _left(self, i: int) -> int | None:
        """Returns left-child-index of given index if exists else None"""
        left = int(2 * i + 1)
        return left if 0 < left < self.size else None

    def _right(self, i: int) -> int | None:
        """Returns right-child-index of given index if exists else None"""
        right = int(2 * i + 2)
        return right if 0 < right < self.size else None

    def _swap(self, i: int, j: int) -> None:
        """Performs changes required for swapping two elements in the heap"""
        # First update the indexes of the items in index map.
        self.pos_map[self.arr[i][0]], self.pos_map[self.arr[j][0]] = (
            self.pos_map[self.arr[j][0]],
            self.pos_map[self.arr[i][0]],
        )
        # Then swap the items in the list.
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _cmp(self, i: int, j: int) -> bool:
        """Compares the two items using default comparison"""
        return self.arr[i][1] < self.arr[j][1]

    def _get_valid_parent(self, i: int) -> int:
        """
        Returns index of valid parent as per desired ordering among given index and
        both it's children
        """
        left = self._left(i)
        right = self._right(i)
        valid_parent = i

        if left is not None and not self._cmp(left, valid_parent):
            valid_parent = left
        if right is not None and not self._cmp(right, valid_parent):
            valid_parent = right

        return valid_parent

    def _heapify_up(self, index: int) -> None:
        """Fixes the heap in upward direction of given index"""
        parent = self._parent(index)
        while parent is not None and not self._cmp(index, parent):
            self._swap(index, parent)
            index, parent = parent, self._parent(parent)

    def _heapify_down(self, index: int) -> None:
        """Fixes the heap in downward direction of given index"""
        valid_parent = self._get_valid_parent(index)
        while valid_parent != index:
            self._swap(index, valid_parent)
            index, valid_parent = valid_parent, self._get_valid_parent(valid_parent)

    def update_item(self, item: int, item_value: int) -> None:
        """Updates given item value in heap if present"""
        if item not in self.pos_map:
            return
        index = self.pos_map[item]
        self.arr[index] = [item, self.key(item_value)]
        # Make sure heap is right in both up and down direction.
        # Ideally only one of them will make any change.
        self._heapify_up(index)
        self._heapify_down(index)

    def delete_item(self, item: int) -> None:
        """Deletes given item from heap if present"""
        if item not in self.pos_map:
            return
        index = self.pos_map[item]
        del self.pos_map[item]
        self.arr[index] = self.arr[self.size - 1]
        self.pos_map[self.arr[self.size - 1][0]] = index
        self.size -= 1
        # Make sure heap is right in both up and down direction. Ideally only one
        # of them will make any change- so no performance loss in calling both.
        if self.size > index:
            self._heapify_up(index)
            self._heapify_down(index)

    def insert_item(self, item: int, item_value: int = None) -> None:
        """Inserts given item with given value in heap"""
        if item_value is None:
            item_value = item
        arr_len = len(self.arr)
        if arr_len == self.size:
            self.arr.append([item, self.key(item_value)])
        else:
            self.arr[self.size] = [item, self.key(item_value)]
        self.pos_map[item] = self.size
        self.size += 1
        self._heapify_up(self.size - 1)

    def get_top(self) -> tuple | None:
        """Returns top item tuple (Calculated value, item) from heap if present"""
        return self.arr[0] if self.size else None

    def extract_top(self) -> tuple | None:
        """
        Return top item tuple (Calculated value, item) from heap and removes it as well
        if present
        """
        top_item_tuple = self.get_top()
        if top_item_tuple:
            self.delete_item(top_item_tuple[0])
        return top_item_tuple


def main():
    heap = Heap()
    for n in [18, 9, 16, 4, 8, 12, 13, 1, 2]:
        heap.insert_item(n)

    print(heap)

    heap.update_item(9, 15)

    print(heap)

    heap.extract_top()

    print(heap)


if __name__ == "__main__":
    main()
