class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        res = []
        for i in range(k):
            max_val = max(hashmap, key=hashmap.get)
            res.append(max_val)
            del hashmap[max_val]

        return res