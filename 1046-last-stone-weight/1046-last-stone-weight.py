class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while(len(stones)>1):
            if(len(stones)<2):
                if(len(stones)==0):
                    return 0
                else:
                    return stones[0]
            else:
                stones.sort()
                res=stones[-1]-stones[-2]
                print(stones)
                stones.pop(-1)
                stones.pop(-1)
                stones.append(res)
        if(len(stones)==0):
            return 0
        else:
            return stones[0]