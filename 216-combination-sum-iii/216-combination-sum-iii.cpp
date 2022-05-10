class Solution {
  vector<vector<int>> result;
    
public:
    vector<vector<int>> combinationSum3(int k, int target) {
        vector<int> buffer;
        vector<int> candidates;
        for(int j=1;j<=9;j++){
            candidates.push_back(j);
            cout<<j;
        }
        dfs(candidates, 0, buffer, 0, target,k);
        return result;
    }
   
    
    void dfs(vector<int> candidates, int i, vector<int>&buffer, int sum, int target,int k){
        if(target == sum && buffer.size()==k){
            result.push_back(buffer);
            return;
        }
        
        if(i>=candidates.size() || sum>target)  return;
        
        buffer.push_back(candidates[i]);
        dfs(candidates, i+1, buffer, sum+candidates[i], target,k);
        buffer.pop_back();
        
        dfs(candidates, i+1, buffer, sum, target,k);
    }
};