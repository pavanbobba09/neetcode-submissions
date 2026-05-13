class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create an unordered map to count the frequency of each element in nums
        unordered_map<int, int> hashing;
        for (auto x : nums) {
            hashing[x]++;
        }

        // Create a vector of pairs (element, frequency)
        vector<pair<int, int>> freqmap;
        for (auto &entry : hashing) {
            freqmap.push_back({entry.second, entry.first});  // {frequency, element}
        }

        // Sort freqmap in descending order of frequency
        sort(freqmap.begin(), freqmap.end(), greater<pair<int, int>>());

        // Collect the top k frequent elements
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(freqmap[i].second);  // freqmap[i].second gives the element
        }

        return result;
    }
};
