from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            temp = [0] * 26
            for char in word:
                temp[ord(char) - ord('a')] += 1
            hash_map.setdefault(tuple(temp), []).append(word)

        return list(hash_map.values())
