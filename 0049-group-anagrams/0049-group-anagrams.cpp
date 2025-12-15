class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // to_string() operation is unlike toupper() and tolower()
        // in maps if u get key pointer or refrence it's different please notice that so basically unordered map is a pair data structure not a map so that's why if u have a key you wont use it as arguemnt key : query_map gives you item key reference
        if(strs.size()==1) return {strs};
        unordered_map<string,vector<string>> query_map;
        for(string s : strs){
            vector<int> query(26,0);
            for(char c: s){
                query[c-'a']+=1;
            }
            string key = "";
            for(int i : query){
                key+=to_string(i)+'.';
            }
            query_map[key].push_back(s);
        }
        vector<vector<string>> ret;
        for(auto& key : query_map){
            ret.push_back(key.second);
        }
        return ret;
    }
};