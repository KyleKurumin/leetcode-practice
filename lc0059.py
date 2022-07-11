class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[n * n]]
        lower = n * n

        while lower > 1:
            lower, upper = lower - len(ans), lower
            ans = [list(range(lower, upper))] + list(map(list, zip(*ans[::-1])))

        return ans