class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            ts=""
            for i in range(0,len(s),k):
                t=s[i:i+k]
                rsum=0
                for j in range(len(t)):
                    rsum+=int(t[j])
                ts+=str(rsum)
            s=ts
        return s