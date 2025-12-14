class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> query;
        for (int i : nums){
            if(query.find(i)!=query.end()){
                return true;
            }
            query.insert(i);
        }
        return false;
    }
};