class Solution {  
    vector<vector<int>> result;
    
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> buffer;
        
        dfs(candidates, 0, buffer, 0, target);
        return result;
    }
    
    void dfs(vector<int> candidates, int i, vector<int>&buffer, int sum, int target){
        if(target == sum){
            result.push_back(buffer);
            return;
        }
        
        if(i>=candidates.size() || sum>target)  return;
        
        buffer.push_back(candidates[i]);
        dfs(candidates, i, buffer, sum+candidates[i], target);
        buffer.pop_back();
        
        dfs(candidates, i+1, buffer, sum, target);
    }
};