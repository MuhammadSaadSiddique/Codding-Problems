class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # MCMXCIIII
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # MCMLXXXXIIII
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # MDCCCCLXXXXIIII
        res=0
        for c in s:
            switch={
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