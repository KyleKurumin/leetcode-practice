# coding=utf-8


# @solution-sync:begin
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        left = 0
        result = 0
        for i in range(len(s)):
            visited[s[i]] = visited.get(s[i], 0) + 1

            while visited[s[i]] > 1:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    visited.pop(s[left])
                left += 1
            result = max(result, i - left + 1)
        return result
# @solution-sync:end


if __name__ == '__main__':
    s = "abcabcbb"

    result = Solution().lengthOfLongestSubstring(s)
    print(result)