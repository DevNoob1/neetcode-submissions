class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> mp;
        for(auto str:strs){
            vector<int> k(26,0);
            for(auto i:str){
                k[i-'a']++;
            }
            string s;
            for (auto i:k){
                s+="#"+to_string(i);
            }
            mp[s].push_back(str);
        }
        vector<vector<string>> ans;
        for(auto i:mp){
            ans.push_back(i.second);
        }
        return ans;
    }
};
