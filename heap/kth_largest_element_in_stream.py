# Pattern: Min Heap of Fixed Size K
# Trigger: "kth largest" + streaming updates = keep only k largest elements

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k

        # convert nums into a heap
        heapq.heapify(self.minHeap)

        # keep only the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # add new value to heap
        heapq.heappush(self.minHeap, val)

        # remove smallest if heap exceeds size k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # root of min heap = kth largest element
        return self.minHeap[0]