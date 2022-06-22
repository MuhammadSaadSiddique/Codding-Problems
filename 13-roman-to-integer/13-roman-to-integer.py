class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        res=0
        for c in s:
            switch={
                'IV':4,
                'IX':9,
                'XC':90,
                'CM':900,
                'I':1,
                'V':5,
                
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
            res+=switch.get(c,0)
        return res