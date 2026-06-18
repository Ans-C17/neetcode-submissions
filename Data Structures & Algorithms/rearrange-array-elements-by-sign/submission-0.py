class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        pos, neg = 0, 0

        for i in range(len(nums)):
            if nums[i] > 0:
                pos = i
                break
            
        for i in range(len(nums)):
            if nums[i] < 0:
                neg = i
                break

        while len(res) < len(nums):
            res.append(nums[pos])
            while pos < len(nums) - 1:
                pos += 1
                if nums[pos] > 0:
                    break
            
            res.append(nums[neg])
            while neg < len(nums) - 1:
                neg += 1
                if nums[neg] < 0:
                    break

        return res
