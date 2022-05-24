class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        map<int, int> mp;
        
        for(int h: hand)
            mp[h]++;
        
        while(!mp.empty()){
            int minVal = mp.begin()->first;
            
            for(int i=minVal; i<minVal+groupSize; i++){
                if(mp.count(i) == 0)    return false;
                
                if(mp[i] == 1)    
                    mp.erase(i);
                else
                    mp[i]--;
            }
        }
        return true;
    }
};