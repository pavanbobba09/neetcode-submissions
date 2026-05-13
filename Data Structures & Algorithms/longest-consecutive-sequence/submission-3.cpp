class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        unordered_set<int> uset(nums.begin(), nums.end());

        int count = 0;
        int element = 0;
        int longest = 0;

        for( auto x: uset){
            if(uset.find(x-1) == uset.end()){
                element = x;
                count = 1;

                while(uset.find(element +1) != uset.end()){
                    element+=1;
                    count+=1;
                }

                longest = max(longest, count);

            }
        }


        return longest;




        
    }
};
