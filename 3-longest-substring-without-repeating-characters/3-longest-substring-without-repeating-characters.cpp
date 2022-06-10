class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int ans = 0;
        unordered_map<int , int> mp;
        
        for(int i = 0, j = 0 ; i < n; i++){
            if(mp.find(s[i]) != mp.end() and mp[s[i]] >= j){
                j = mp[s[i]]+1;
            }
            ans = max(ans, i-j+1);
            mp[s[i]] = i;
        }
        return ans;

    }
};