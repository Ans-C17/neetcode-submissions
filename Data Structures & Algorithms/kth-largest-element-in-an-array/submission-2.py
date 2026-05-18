class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for i in range(1, k):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)