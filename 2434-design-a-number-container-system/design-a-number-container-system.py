class NumberContainers:

    def __init__(self):
        self.container = {}
        self.numbers = {}

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        if number not in self.numbers:
            self.numbers[number] = []
        heapq.heappush(self.numbers[number],index)
        

    def find(self, number: int) -> int:
        if number not in self.numbers:
            return -1

        heap = self.numbers[number]
        while heap:
            index = heap[0]
            if self.container[index]==number:
                return index
            heapq.heappop(heap)

        return -1

        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
