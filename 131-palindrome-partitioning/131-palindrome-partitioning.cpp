class Solution {
    vector<vector<string>> res;
    
public:
    vector<vector<string>> partition(string s) {
        vector<string> path;
        helper(0, s, path);
        return res;
    }
    
    void helper(int i, string s, vector<string> path){
        if(i == s.size()){
            res.push_back(path);
            return;
        }
        
        for(int j=i; j<s.size(); j++){
            if(isPalindrome(s, i, j)){
                path.push_back(s.substr(i, j-i+1));
                helper(j+1,s, path);
                path.pop_back();
            }
        }
            
    }
    
    bool isPalindrome(string s, int start, int end){
        while(start<=end){
            if(s[start++] != s[end--])  return false;
        }
        return true;
    }
};