class Solution {
 vector<vector<int>> result;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> buffer;
        dfs(0, buffer, nums);
        return result;
    }
    
    void dfs(int index, vector<int>&buffer, vector<int>&nums){
        result.push_back(buffer);
        
        
        for(int i=index; i<nums.size(); i++){
            buffer.push_back(nums[i]);
            dfs(i+1, buffer, nums);
            buffer.pop_back();
        }
        
       return;     
    }
};