class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def heapifyUp(self, i):
        while i > 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def heapifyDown(self, i):
        minIndex = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left < len(self.heap) and self.heap[left][0] < self.heap[minIndex][0]:
            minIndex = left

        if right < len(self.heap) and self.heap[right][0] < self.heap[minIndex][0]:
            minIndex = right

        if i != minIndex:
            self.heap[i], self.heap[minIndex] = self.heap[minIndex], self.heap[i]
            self.heapifyDown(minIndex)

    def insert(self, value, label):
        element = [value, label]
        self.heap.append(element)
        self.heapifyUp(len(self.heap) - 1)

    def extractMin(self):
        if not self.heap:
            return None

        minVal = self.heap[0]
        lastElement = self.heap.pop()

        if self.heap:
            self.heap[0] = lastElement
            self.heapifyDown(0)

        return minVal

    def peekMin(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return len(self.heap) == 0
