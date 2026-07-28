class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0 
        prefix = {0:1}
        totalSum = 0 

        for i in nums:
            totalSum+=i
            removal = totalSum - k 
            if removal in prefix:
                total+=prefix[removal]

            prefix[totalSum] = prefix.get(totalSum,0)+1

        return total