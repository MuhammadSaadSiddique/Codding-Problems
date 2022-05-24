class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int groupSize) {
        map<int, int> mp;
        
        for(int h: nums)
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