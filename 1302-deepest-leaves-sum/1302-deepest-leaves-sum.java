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
    public int deepestLeavesSum(TreeNode root) {
        dfs(root,0,0);
        
         // Set set = map.entrySet();
         //  // Get an iterator
         //  Iterator i = set.iterator();
         //  // Display elements
         //  while(i.hasNext()) {
         //     Map.Entry me = (Map.Entry)i.next();
         //     System.out.print(me.getKey() + ": ");
         //     System.out.println(me.getValue());
         //  }
      
        return map.get(maxdepth);
    }
    HashMap<Integer, Integer> map = new HashMap<>();
    
    int maxdepth = Integer.MIN_VALUE;
    
    
    public void dfs(TreeNode root, int depth, int position){
        if(root == null)return;
        if(!map.containsKey(depth)){
            map.put(depth,root.val);
            maxdepth=depth;
            //System.out.println(root.val);
            //sum+=root.val;
        }
        else{
            int sum=map.get(depth);
            sum=sum+root.val;
            map.put(depth,sum);
        }
       
        //maxWidth = Math.max(maxWidth, position-map.get(depth)+1);
        dfs(root.left, depth+1, 2*position);
        dfs(root.right,depth+1, 2*position+1);
        
    }
}