class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I': 1,
            'IV':4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L':50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        answer = 0
        if 'IV' in s:
            answer += values['IV']
            s = s.replace('IV','')
        if 'IX'in s:
            answer += values['IX']
            s = s.replace('IX','')
        if 'XL'in s:
            answer += values['XL']
            s = s.replace('XL','')
        if 'XC'in s:
            answer += values['XC']
            s = s.replace('XC','')
        if 'CD'in s:
            answer += values['CD']
            s = s.replace('CD','')
        if 'CM'in s:
            answer += values['CM']
            s = s.replace('CM','')
        s = list(s)
        for n in s:
            answer += values[n]
        return answer
    
s = 'MCMXCIV'
h = Solution()
print(h.romanToInt(s))