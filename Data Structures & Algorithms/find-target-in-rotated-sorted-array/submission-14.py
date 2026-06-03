class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            
            if target == nums[m]:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]: # i.e right side
                    l = m + 1
                else: # i.e between l and m
                    r = m - 1
            else: # l will always be left of m, so this is right part
                if target < nums[m] or target > nums[r]: # left side
                    r = m - 1
                else:
                    l = m + 1

        return -1