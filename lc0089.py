class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = ['0', '1']
        for i in range(1, n):
            tmp = []
            for item in res[::-1]:
                tmp.append('1' + item.zfill(i))
            res += tmp

        for idx, item in enumerate(res):
            res[idx] = int(item, 2)

        return res