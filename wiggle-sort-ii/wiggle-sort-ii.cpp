class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n = nums.size();
        auto mid_it = nums.begin() + n / 2;
        nth_element(nums.begin(), mid_it, nums.end());
        int middle = *mid_it;
        #define A(i) nums[(1 + (i) * 2) % (n | 1)]
        int i = 0, j = 0, k = n - 1;
        while (j <= k) {
            if (A(j) > middle) swap(A(i++), A(j++));
            else if (A(j) < middle) swap(A(j), A(k--));
            else ++j;               
        }
    }
};