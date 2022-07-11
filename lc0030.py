# coding=utf-8

# @solution-sync:begin
import collections
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        counter = collections.Counter(words)

        base_length = len(words[0])

        ans = []
        record = {}

        for i in range(base_length):
            temp = s[i: i + n * base_length]
            record[i] = self.construct(temp, base_length)
            if collections.Counter(record[i]) == counter:
                ans.append(i)

        for i in range(base_length, len(s), base_length):
            for j in range(base_length):
                if i + j + n * base_length > len(s):
                    break
                tmp = s[i + j: i + j + n * base_length]
                record[j].pop(0)
                record[j].append(tmp[-base_length:])
                if collections.Counter(record[j]) == counter:
                    ans.append(i + j)
        return ans

    def construct(self, s, base_length):
        tmp = []
        for i in range(0, len(s), base_length):
            string = s[i:i + base_length]
            tmp.append(string)
        return tmp
# @solution-sync:end


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]

    result = Solution().findSubstring(s, words)
    print(result)