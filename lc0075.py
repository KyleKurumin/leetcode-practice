class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        helper = [[], [], []]

        for num in nums:
            helper[num].append(num)

        i = 0
        for stack in helper:
            while stack:
                nums[i] = stack.pop()
                i += 1
