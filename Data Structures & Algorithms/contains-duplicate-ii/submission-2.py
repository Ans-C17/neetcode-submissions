class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = {}
        for i in range(len(nums)):
            if nums[i] in s:
                if abs(s[nums[i]] - i) <= k:
                    return True
                s[nums[i]] = i
            else:
                s[nums[i]] = i
        
        return False