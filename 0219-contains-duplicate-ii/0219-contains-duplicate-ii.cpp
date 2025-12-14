class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        // ok so I need to iterate and update my closest index
        unordered_map<int,int> query;
        int n = nums.size();
        for(int i=0; i<n; i++){
            if(query.find(nums[i])!=query.end()){
                if(i-query[nums[i]]<=k){
                    return true;
                }else{
                    query[nums[i]]=i;
                }
            }else{
                query[nums[i]]=i;
            }
        }
        return false;
    }
};