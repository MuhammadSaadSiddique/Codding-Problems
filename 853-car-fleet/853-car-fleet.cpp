class Solution {
public:
    int carFleet(int target, vector<int>& pos, vector<int>& speed) {
        map<int, float> map;
        
        for(int i=0; i<pos.size(); i++)
            map[-pos[i]] = (double)(target-pos[i])/speed[i];
        
        int count = 0;
        
        float curMax = 0;
        
        for(auto it: map){
            if(it.second > curMax){
                count++;
                curMax = it.second;
            }
        }
        return count;
    }
};