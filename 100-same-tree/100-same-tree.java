/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        dfs(p,q,0,0);
        return flag;
    }
    Boolean flag=true;
    public void dfs(TreeNode p,TreeNode q, int depth, int position){
        if(p == null && q!=null) {
            flag=false;
            return;
        }
        if (p!=null && q==null) {
            flag=false;
            return;
        }
        if (p==null && q== null) return;
        if (p.val!=q.val){
            flag=false;
            return;
        }
       
        dfs(p.left,q.left, depth+1, 2*position);
        dfs(p.right,q.right,depth+1, 2*position+1);
        //flag=true;
        
    }
}