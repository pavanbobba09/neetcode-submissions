class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> umap1;
        unordered_map<char, int> umap2;
        if (s.size() != t.size()) {
            return false;
        }

        for( int i=0;i<s.size();i++){
            umap1[s[i]]++;
            umap2[t[i]]++;
        }

        for( int y=0;y<umap1.size();y++){
            if(umap1[y] != umap2[y]){
                return false;
            }

        }
        return true;
        
    }

};
