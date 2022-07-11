# coding=utf-8


# @solution-sync:begin
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        temp = ['' for _ in range(numRows)]

        flg = -1
        idx = 0

        for char in s:
            if idx == 0 or idx == numRows - 1:
                flg = -flg

            temp[idx] += char
            idx += flg

        return ''.join(temp)
# @solution-sync:end


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3

    result = Solution().convert(s, numRows)
    print(result)