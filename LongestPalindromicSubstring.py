class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return ''
        ans = s[0]
        flag = False
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i):
                pal = s[j:j+i+1]
                if pal == pal[::-1]:
                    ans = pal
                    flag = True
                    break
            if flag:
                break
                
        return ans