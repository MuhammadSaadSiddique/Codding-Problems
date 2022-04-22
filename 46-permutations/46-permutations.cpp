class Solution {
    vector<vector<int>> result;
public:
    vector<vector<int>> permute(vector<int>& nums) {
        if(nums.size() == 0)  return result;
        
        vector<int> buffer;
        vector<bool> used(nums.size(), false);
        
        helper(nums, buffer, used);
        return result;
    }
    
    void helper(vector<int>&nums, vector<int> &buffer, vector<bool>&used){
        if(buffer.size() == nums.size()){
            result.push_back(buffer);
            return;
        }
        
        for(int i=0; i<nums.size(); i++){
            if(used[i] == true) continue;
            
            used[i] = true;
            
            buffer.push_back(nums[i]);
            helper(nums, buffer, used);
            buffer.pop_back();
            used[i] = false;
        }
    }
};