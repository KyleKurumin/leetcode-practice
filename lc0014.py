# coding=utf-8

from typing import List

# @solution-sync:begin
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for item in zip(*strs):
            if len(list(set(item))) == 1:
                prefix += item[0]
            else:
                break
        return prefix
# @solution-sync:end


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]

    result = Solution().longestCommonPrefix(strs)
    print(result)
