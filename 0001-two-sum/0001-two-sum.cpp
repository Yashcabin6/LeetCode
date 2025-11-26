class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n= nums.size();
        unordered_map<int,int> a;
        for(int i=0; i<n; i++){
            auto it= a.find(target-nums[i]);
            if(it!=a.end()){
                return {i,it->second};
            }else{
                a.insert({nums[i],i});
            }
            
        }
        vector<int> ret1(2,0);
        return ret1;
    }
};