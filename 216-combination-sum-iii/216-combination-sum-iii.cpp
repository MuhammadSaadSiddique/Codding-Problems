class Solution {
  vector<vector<int>> result;
    
public:
    vector<vector<int>> combinationSum3(int k, int target) {
        vector<int> buffer;
        
        dfs( 1, buffer, 0, target,k);
        return result;
    }
   
    
    void dfs( int i, vector<int>&buffer, int sum, int target,int k){
        if(target == sum && buffer.size()==k){
            result.push_back(buffer);
            return;
        }
        
        if(i>9 || sum>target)  return;
        
        buffer.push_back(i);
        dfs( i+1, buffer, sum+i, target,k);
        buffer.pop_back();
        
        dfs( i+1, buffer, sum, target,k);
    }
};