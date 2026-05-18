class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        
        mashhap = {}
        for letter in t:
            mashhap[letter] = mashhap.get(letter, 0) + 1

        if len(hashmap) != len(mashhap):
            return False

        for letter in s:
            if hashmap[letter] != mashhap.get(letter, -1):
                return False
        
        return True
            