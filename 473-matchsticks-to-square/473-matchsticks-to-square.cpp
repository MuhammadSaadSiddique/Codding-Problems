class Solution {
public:
    bool makesquare(vector<int>& matchsticks) {
        int sum=0;
        for(int s:matchsticks)
            sum += s;
        
        int length = sum/4;
        
        vector<int> sides(4, 0);
        
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        
        if(sum%4 != 0)   return false;
        
        return helper(0, matchsticks, sides, length);
    }
    
    bool helper(int i, vector<int> &matchsticks, vector<int>&sides, int length){
        if(i == matchsticks.size()) return true;
        
        for(int j=0; j<4; j++){
            if(sides[j] + matchsticks[i] <= length){
                sides[j] += matchsticks[i];
                
                if(helper(i+1, matchsticks, sides, length)) return true;
                
                sides[j] -= matchsticks[i];
            }
        }
        return false;
    }
};