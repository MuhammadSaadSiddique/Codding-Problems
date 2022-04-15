class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(20, -1);
        
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        
        numTrees(n, dp);
        return dp[n];
    }
    
    int numTrees(int n, vector<int>&dp){
        if(n==0)    return 1;
        if(n<=2)    return n;
        
        if(dp[n] != -1) return dp[n];
        
        int sum = 0;
        
        for(int i=1; i<=n; i++){
            sum += numTrees(i-1, dp) * numTrees(n-i, dp);
        }
        
        dp[n] = sum;
        
        return dp[n];
    }
};