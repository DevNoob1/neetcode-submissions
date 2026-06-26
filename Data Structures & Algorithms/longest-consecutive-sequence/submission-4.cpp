class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int>nset(nums.begin(),nums.end());
        int m=0;
        for (auto i:nums){
            if(!nset.count(i-1)){
                int c=i;
                int l=1;
                while(nset.count(c+1)){
                    c++;
                    l+=1;
                    }
            m=max(l, m); 
                }
        }
        return m;
    }
};
