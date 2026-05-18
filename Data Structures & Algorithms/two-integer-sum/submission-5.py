class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            if target - nums[i] not in hashmap:
                hashmap[nums[i]].append(i)
            else:
                return [hashmap[target - nums[i]][0], i]