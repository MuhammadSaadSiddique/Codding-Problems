class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res=[]
        for n in ops:
            if n =="+":
                res.append(res[-1]+res[-2])
            elif n =="D":
                res.append(res[-1]*2)
            elif n=="C":
                res.pop()
            else:
                res.append(int(n))
       
        return sum(res)