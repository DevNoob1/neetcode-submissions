class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length()!=t.length()) return false;
        vector <int> a(26,0);
        for (auto i:s) a[i-'a']++;
        for (auto i:t) a[i-'a']--;
        for (auto i:a){
            if (i!=0) return false;
        }
        return true;
        // cout<<'r'-'a';
    }
};
