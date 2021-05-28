class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        spl = str.split()
        if len(spl) != len(pattern):return False
        newDict = dict()
        length = len(spl)
        for x in range(length):
            if pattern[x] not in newDict:
                if spl[x] in newDict.values():return False
                newDict[pattern[x]] = spl[x]
            else:
                if newDict[pattern[x]] != spl[x]:
                    return False
        return True