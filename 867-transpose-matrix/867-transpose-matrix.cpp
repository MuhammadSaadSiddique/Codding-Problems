class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        vector<vector<int>> ans;
        int R = A.size(), C = A[0].size();
        //vector<> ans = new int[C][R];
        for (int c = 0; c < C; ++c) {
            vector<int> v1;
             for (int r = 0; r < R; ++r){
                v1.push_back( A[r][c]);
            }
            ans.push_back(v1);
        }
        return ans;
    }
};