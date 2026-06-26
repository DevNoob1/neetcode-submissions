class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        vector<int>ans;
        for (auto i:nums){
            mp[i]++;
        }
        for (auto i:mp) {
            cout<< i.first<<":"<<i.second<<" ";

        }
        vector <pair<int,int>> vp;
        for (auto i:mp){
            vp.push_back({i.second, i.first});
        }
        sort(vp.begin(),vp.end());
        for (int i=vp.size()-1;i>=0 && k>0;i--,k--) ans.push_back(vp[i].second);
    return ans; 
    }
};
