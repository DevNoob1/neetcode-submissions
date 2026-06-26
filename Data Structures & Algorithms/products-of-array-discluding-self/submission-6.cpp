class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>out(nums.size(),1);
        int p=1;int s=1;
        for(int i=0;i<nums.size();i++){
            out[i]=p;
            p*=nums[i];
        }
        for(int i=nums.size()-1;i>=0;i--){
            out[i]*=s;
            s*=nums[i];
        }
        return out;
    }
};
