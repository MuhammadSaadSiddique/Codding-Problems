class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        from collections import Counter
        data = Counter(tasks)
        d2 = Counter(data)
        #data = sorted(data.elements)
        c=0
        while len(data)>0:
            for k,val in data.items():
                if val < 2:
                    return -1
                else:
                    if val<3:
                        c+=1
                        del d2[k]
                    else:
                        c += 1
                        if val%3==0 or val%3==2 :
                            d2[k] = d2[k]-3
                        else:
                            d2[k] = d2[k]-2
                        if(d2[k]==0):
                            del d2[k]

            data=Counter(d2)
        return c
        