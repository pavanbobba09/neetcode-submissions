class Solution {
public:
    bool isPalindrome(string s) {
        

        vector<char> strings;

        for (char c : s) {
            if (isalnum(c)) {
                strings.push_back(tolower(c));
            }
        }
        int left = 0;
        int right = strings.size() - 1;

        while (left < right) {
            if (strings[left] != strings[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
