class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ch = s.strip().rsplit(' ')[-1]
        return len(ch)