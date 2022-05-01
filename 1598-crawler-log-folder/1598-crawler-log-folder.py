class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        c=0
        res=[]
        for log in logs:
            if log!="../" and log!="./":
                c+=1
            elif  log=="../":
                if c>0:
                    c-=1
        return c