class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        freCountB = collections.defaultdict(int)
        def getfcount(word):
            freCount = collections.defaultdict(int)
            for c in word:
                freCount[c]+=1
            return freCount
        for b in B:
            freCount = getfcount(b)
            for c in freCount:
                freCountB[c] = max(freCount[c], freCountB[c])
        ret = []
        for a in A:
            freCount = getfcount(a)
            match = True
            for c in freCountB:
                if freCount[c] < freCountB[c]:
                    match = False
                    break
            if match:
                ret.append(a)
        return ret