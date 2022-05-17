/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
   queue<TreeNode*> q; 
public:
    int deepestLeavesSum(TreeNode* root) {
        int sum=0;
        q.push(root);
        while(!q.empty()){
            int size=q.size();
            sum=0;
            for(int i=0;i<size;i++){
                TreeNode* p=q.front();
                q.pop();
                
                sum+=p->val;
                if(p->right){
                   q.push(p->right); 
                }
                if(p->left){
                   q.push(p->left); 
                }
            }
        }
        return sum;
    }
};