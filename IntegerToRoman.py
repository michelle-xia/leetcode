class Solution:
    def intToRoman(self, num):
        res = ''
        if num >= 1000:
            mult = num // 1000
            res += 'M' * mult
            num %= 1000
        if num >= 900:
            res += 'CM'
            num -= 900
        if num >= 500:
            mult =  num // 500
            res += 'D' * mult
            num %= 500
        if num >= 400:
            res += 'CD'
            num -= 400
        if num >= 100:
            mult = num // 100
            res += 'C' * mult
            num %= 100
        if num >= 90:
            mult = num // 90
            res += 'XC'
            num %= 90
        if num >= 50:
            mult = num // 50
            res += 'L' * mult
            num %= 50
        if num >= 40:
            mult = num // 40
            res += 'XL'
            num %= 40
        if num >= 10:
            mult = num // 10
            res += 'X' * mult
            num %= 10
        if num >= 9:
            res += 'IX'
            num -= 9
        if num >= 5:
            mult = num // 5
            res += 'V' * mult
            num %= 5
        if num >= 4:
            res += 'IV'
            num %= 4
        res += 'I' * num
        return res

# recursive solution
class Solution2:
    def intToRoman(self, num):
        d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        if num == 0:
            return ''
        
        for k in d.keys():
            if num - k >= 0:
                return d[k] + self.intToRoman(num - k)