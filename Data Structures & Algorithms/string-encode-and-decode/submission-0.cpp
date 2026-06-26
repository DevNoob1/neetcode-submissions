class Solution {
public:

    string encode(vector<string>& strs) {
        string str;
        for(auto i:strs){
            str+=to_string(i.size())+"#"+i;
        }
        return str;

    }

    vector<string> decode(string s) {
        vector<string> st;
        int i=0;
        while(i<s.size()){
            int j=i;
            while(s[j]!='#')j++;
            int len=stoi(s.substr(i,j-i));
            string word =s.substr(j+1,len);
            st.push_back(word);
            i=1+j+len;
        }
        return st;
    }
};
