class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            return self.addBinary(b, a)

        a = a[::-1]
        b = b[::-1]

        res = [0] * (len(a) + 1)

        add = 0
        for i in range(len(res)):
            temp = add
            if i < len(a):
                temp += int(a[i])
            if i < len(b):
                temp += int(b[i])

            add = temp // 2
            value = temp % 2
            res[i] = value

        res = res[::-1]
        if res[0] == 0:
            res = res[1:]

        return ''.join(map(lambda x: str(x), res))