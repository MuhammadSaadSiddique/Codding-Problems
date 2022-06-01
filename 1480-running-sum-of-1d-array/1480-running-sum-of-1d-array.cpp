class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result;
        for(auto num:nums){
            if(result.size()==0)
                result.push_back(num);
            else
                result.push_back(result.back()+num);
        }
        return result;
    }
};