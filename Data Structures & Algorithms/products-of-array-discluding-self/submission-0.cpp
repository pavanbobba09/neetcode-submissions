class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1); // Initialize the result array

        // Brute force approach: Calculate product for each element
        for (int i = 0; i < n; i++) {
            int product = 1;
            for (int j = 0; j < n; j++) {
                if (i != j) { // Skip the current element
                    product *= nums[j];
                }
            }
            result[i] = product;
        }

        return result;
    }
};
