class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noel = {}
        for i in range(len(nums)):
            if nums[i] in noel:
                return True
            noel[nums[i]] = 1 + noel.get(nums[i], 0)
        return False