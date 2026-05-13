class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> umap;

        for( auto x: nums){
            umap[x]++;
        }

        for(auto &x2: umap){
            if(x2.second>1){
                return true;
            } 
        }

        return false;

        

    }
};
