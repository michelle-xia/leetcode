class Solution:
    def reverse(self, x):
        if x is None:
            return
        if x < 0:
            x *= -1
            x = str(x)
            x = x[::-1]
            return int(x) * -1 if int(x) * -1 > -2 ** 31 else 0
        else:
            x = str(x)
            x = x[::-1]
            return int(x) if int(x) < 2 ** 31 - 1 else 0