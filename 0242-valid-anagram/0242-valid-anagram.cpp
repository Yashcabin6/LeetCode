class Solution {
public:
    bool isAnagram(string s, string t) {
        // I need a fking counter array to count elements but first I check if size is equal or no
        if(s.size()!=t.size()){
            return false;
        }
        vector<int> query(26,0);
        for(int i= 0; i<s.size();i++){
            query[s[i]-'a']+=1;
            query[t[i]-'a']-=1;
        }
        for(int i : query){
            if(i!=0) return false;
        }
        return true;
    }
};