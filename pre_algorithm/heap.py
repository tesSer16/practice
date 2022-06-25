class Heap:
    def __init__(self):
        self._data = [0] * 100
        self._size = 0

    def heappush(self, x):
        self._size += 1
        if len(self._data) == self._size:
            self._data.extend([0] * len(self._data))

        hole = self._size
        while hole != 1:
            if self._data[hole // 2] < x:
                break
            self._data[hole] = self._data[hole // 2]
            hole //= 2
        self._data[hole] = x

    def heappop(self):
        temp = self._data[1]
        self._data[1] = self._data[self._size]
        self._size -= 1
        self.heapify(1)

        return temp

    def make_heap(self):
        for i in range(self._size // 2):
            self.heapify(i + 1)

    def heapify(self, index):
        idx = index
        temp = self._data[index]
        while idx < self._size:
            left, right = 2 * idx, 2 * idx + 1
            child = left
            if left > self._size:
                break
            if right <= self._size and self._data[right] < self._data[left]:
                child = right

            if temp < self._data[child]:
                break

            self._data[idx] = self._data[child]
            idx = child

        self._data[idx] = temp

    def __len__(self):
        return self._size

    def print(self):
        print(*self._data[1:self._size + 1])


if __name__ == "__main__":
    N = 9
    arr = [3, 1, 4, 5, 9, 2, 6, 8, 7]
    heap = Heap()
    for a in arr:
        heap.heappush(a)
    heap.print()
    result = []
    for _ in range(9):
        result.append(heap.heappop())
        heap.print()
    print(result)
