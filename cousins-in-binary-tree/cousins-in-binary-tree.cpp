/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isCousins(TreeNode* root, int x, int y) {
      if(root->val == x && root->val == y)
            return false;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode *x_parent = NULL, *y_parent = NULL;
        int qSize = q.size();
        while(!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            --qSize;
            if(curr->left) {
                q.push(curr->left);
                if(curr->left->val == x) {
                    x_parent = curr;
                }
                if(curr->left->val == y) {
                    y_parent = curr;
                }
            }
            if(curr->right) {
                q.push(curr->right);
                if(curr->right->val == x) {
                    x_parent = curr;
                }
                if(curr->right->val == y) {
                    y_parent = curr;
                }
            }
            if(qSize == 0) {
                if(x_parent || y_parent)
                    break;
                qSize = q.size();
            }
        }        
        return x_parent && y_parent && x_parent != y_parent; 
    }
};
