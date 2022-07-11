class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j])
                div = product // 10
                mod = product % 10
                res[i + j + 1] += mod
                res[i + j] += div

        for i in range(len(res) - 1, 0, -1):
            res[i - 1] += res[i] // 10
            res[i] = res[i] % 10

        idx = 0
        while idx < len(res) and res[idx] == 0:
            idx += 1

        return ''.join(map(lambda x: str(x), res[idx:])) if idx < len(res) else '0'
    