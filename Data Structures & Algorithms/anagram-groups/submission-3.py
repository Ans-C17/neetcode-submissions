class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            frequency_list = [0] * 26

            for letter in word:
                frequency_list[ord(letter) - ord('a')] += 1
            
            hashmap[tuple(frequency_list)] = hashmap.get(tuple(frequency_list), []) + [word]
            
        return list(hashmap.values())
            
            
        