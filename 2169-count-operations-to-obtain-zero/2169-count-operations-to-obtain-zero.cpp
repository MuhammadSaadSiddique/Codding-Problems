class Solution {
public:
    int countOperations(int num1, int num2) {
        int step=0;
        while(num1!=0 and num2!=0){
            if(num1 < num2)
                num2-=num1;
            else
                num1-=num2;
            step++;
        }
        return step;
    }
};